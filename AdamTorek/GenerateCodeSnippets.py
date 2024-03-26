from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AwqConfig
from itertools import islice

import torch
from evalplus.data import get_mbpp_plus, get_human_eval_plus, write_jsonl
from enum import Enum

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
        inputs = tokenizer(prompts, return_tensors="pt", padding=True).to(device)
        outputs = model.generate(**inputs, 
                        do_sample=True, 
                         temperature=0.1, 
                         top_p=0.9, 
                         num_return_sequences = 1, 
                         eos_token_id = tokenizer.eos_token_id, 
                         pad_token_id = tokenizer.eos_token_id,
                         max_length=2048)
        return tokenizer.batch_decode(outputs, skip_special_tokens=True)

def gen_dataset_samples(dataset, model, tokenizer, device, quantize):
    
    batch_size = 1
    if quantize != QuantizeType.NONE:
        batch_size = 4
   
    results = []
    for batch in chunked(dataset.items(), batch_size):
        prompts = []
        task_ids = []
        for problem in batch:
            prompts.append(problem[1]["prompt"])
            task_ids.append(problem[0])
        outputs = generate_code(prompts, model, tokenizer, device)
        for i in range(0, batch_size):
            results.append(dict(task_id = task_ids[i], solution=outputs[i]))
    
    return results



def main():
    models = {"none":{"CodeLlama":"codellama/CodeLlama-7b-hf",
                    "WizardCoder":"WizardLM/WizardCoder-3B-V1.0",
                    "StarCoder2":"bigcode/starcoder2-7b",
                    "Mistral":"mistralai/Mistral-7B-Instruct-v0.2"},
            "8_bit":{"CodeLlama":"TheBloke/CodeLlama-7B-AWQ",
                    "WizardCoder":"WizardLM/WizardCoder-3B-V1.0",
                    "StarCoder2":"bigcode/starcoder2-7b",
                    "Mistral":"TheBloke/Mistral-7B-Instruct-v0.1-AWQ"}}
    quantize = QuantizeType.EIGHT_BIT
    device = "cuda"
    model_id = "TheBloke/CodeLlama-7B-AWQ"
    q_conf = None

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.bos_token

    if quantize != QuantizeType.NONE:
        if quantize == QuantizeType.EIGHT_BIT:
            q_conf = AwqConfig(weights="int8")
        elif quantize == QuantizeType.FOUR_BIT:
            q_conf = AwqConfig(weights="int4")
    
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, quantization_config=q_conf)
    model.to(device)
    model.config.pad_token_id = model.config.bos_token_id

    humaneval_results = gen_dataset_samples(get_human_eval_plus(), model, tokenizer, device, quantize)
    mbpp_results = gen_dataset_samples(get_mbpp_plus(), model, tokenizer, device, quantize)

    write_jsonl("humaneval_" + get_output_name(model_id, quantize) + "" + ".jsonl", humaneval_results)
    write_jsonl("mbpp_" + get_output_name(model_id, quantize) + "" + ".jsonl", mbpp_results)

if __name__ == "__main__":
    main()