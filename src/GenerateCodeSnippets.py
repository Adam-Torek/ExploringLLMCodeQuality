from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AwqConfig
from itertools import islice

import torch
from evalplus.data import get_mbpp_plus, get_human_eval_plus, write_jsonl
from enum import Enum
import os

class QuantizeType(Enum):
    NONE = 0
    EIGHT_BIT = 1
    FOUR_BIT = 2

def chunked(it, size):
    it = iter(it)
    while True:
        p = tuple(islice(it, size))
        if not p:
            break
        yield p


def get_output_name(model_name, quantization):
    model_name = model_name.split("/")[1]
    if quantization == QuantizeType.EIGHT_BIT:
        model_name += "_8_bit"
    elif quantization == QuantizeType.FOUR_BIT:
        model_name += "_4_bit"
    return model_name

def generate_code(prompts, model, tokenizer, device):
        inputs = tokenizer(prompts, return_tensors="pt", padding_side="left", padding=True).to(device)
        outputs = model.generate(**inputs, 
                        do_sample=True, 
                         temperature=0.1, 
                         top_p=0.9, 
                         num_return_sequences = 1, 
                         eos_token_id = tokenizer.eos_token_id, 
                         pad_token_id = tokenizer.eos_token_id,
                         max_length=1024)
        return tokenizer.batch_decode(outputs, skip_special_tokens=True)

def gen_dataset_samples(dataset, model, tokenizer, device, quantize):
    
    batch_size = 1
    if quantize != QuantizeType.EIGHT_BIT:
        batch_size = 4
   
    results = []
    for batch in chunked(dataset.items(), batch_size):
        prompts = []
        task_ids = []
        for problem in batch:
            prompts.append(problem[1]["prompt"])
            task_ids.append(problem[0])
        outputs = generate_code(prompts, model, tokenizer, device)
        for i in range(0, len(batch)):
            results.append(dict(task_id = task_ids[i], solution=outputs[i]))
    
    return results



def main():
    model_keys = ["CodeLlama",
                    "WizardCoder",
                    "StarCoder2", 
                    "Mistral"]
    
    models_standard = {"CodeLlama":"codellama/CodeLlama-7b-hf",
                    "WizardCoder":"vanillaOVO/WizardCoder-Python-7B-V1.0",
                    "StarCoder2":"bigcode/starcoder2-7b",
                    "Mistral":"mistralai/Mistral-7B-Instruct-v0.2"}
    
    models_quantized = {"CodeLlama":"TheBloke/CodeLlama-7B-AWQ",
                    "WizardCoder":"TheBloke/WizardCoder-Python-7B-V1.0-AWQ",
                    "StarCoder2":"models_quantized/starcoder2-7b-awq",
                    "Mistral":"TheBloke/Mistral-7B-Instruct-v0.1-AWQ"}
    
    results_folder = "generated_code"
    
    device = "cuda" if torch.cuda.is_available() else "cpu"

    for quantization in QuantizeType:
        for model_name in model_keys:
        
            model_id = models_standard[model_name]
            q_conf = None
            if quantization != QuantizeType.NONE:
                model_id = models_quantized[model_name]
                if quantization == QuantizeType.EIGHT_BIT:
                    q_conf = AwqConfig(weights="int8")
                elif quantization == QuantizeType.FOUR_BIT:
                    q_conf = AwqConfig(weights="int4")

            tokenizer = AutoTokenizer.from_pretrained(model_id, padding_size="left")
            tokenizer.pad_token = tokenizer.bos_token
            
            model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, quantization_config=q_conf)
            model.to(device)
            model.config.pad_token_id = model.config.bos_token_id

            human_eval_output_name = "humaneval_" + get_output_name(model_id, quantization) + "" + ".jsonl"
            mbpp_eval_output_name = "mbpp_" + get_output_name(model_id, quantization) + "" + ".jsonl"
            human_eval_output_path = os.path.join(results_folder, human_eval_output_name)
            mbpp_eval_output_path = os.path.join(results_folder, mbpp_eval_output_name)
            if not os.path.exists(human_eval_output_path):
                humaneval_results = gen_dataset_samples(get_human_eval_plus(), model, tokenizer, device, quantization)
                write_jsonl(human_eval_output_path, humaneval_results)

            if not os.path.exists(mbpp_eval_output_path):
                mbpp_results = gen_dataset_samples(get_mbpp_plus(), model, tokenizer, device, quantization)
                write_jsonl(mbpp_eval_output_path, mbpp_results)

if __name__ == "__main__":
    main()