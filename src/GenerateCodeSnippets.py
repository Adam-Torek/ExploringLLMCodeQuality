from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import BitsAndBytesConfig

import torch
from evalplus.data import get_mbpp_plus, get_human_eval_plus, write_jsonl
from enum import Enum

class QuantizeType(Enum):
    NONE = 0
    EIGHT_BIT = 1
    FOUR_BIT = 2


def get_output_name(model_name, quantization):
    model_name = model_name.split("/")[1]
    if quantization == QuantizeType.EIGHT_BIT:
        model_name += "_8_bit"
    elif quantization == QuantizeType.FOUR_BIT:
        model_name += "_4_bit"
    return model_name

def generate_code(prompt, model, tokenizer, device):
        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
        outputs = model.generate(inputs, 
                        do_sample=True, 
                         temperature=0.1, 
                         top_p=0.9, 
                         num_return_sequences = 1, 
                         eos_token_id = tokenizer.eos_token_id, 
                         pad_token_id = tokenizer.eos_token_id,
                         max_length=1024)
        return tokenizer.decode(outputs[0])

def gen_dataset_samples(dataset, model, tokenizer, device):
    return [
        dict(task_id=task_id, solution=generate_code(problem["prompt"], model, tokenizer, device))
        for task_id, problem in dataset.items()
    ]

def main():
    quantize = QuantizeType.EIGHT_BIT
    device = "cuda"
    model_id = "codellama/CodeLlama-7b-hf"
    model = None
    q_conf = None
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    if quantize != QuantizeType.NONE:
        if quantize == QuantizeType.EIGHT_BIT:
            q_conf = BitsAndBytesConfig(load_in_8bit=True)
        elif quantize == QuantizeType.FOUR_BIT:
            q_conf = BitsAndBytesConfig(load_in_4bit=True)
    
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, quantization_config=q_conf)
    if quantize == QuantizeType.NONE:
        model.to(device)

    humaneval_results = gen_dataset_samples(get_human_eval_plus(), model, tokenizer, device)
    mbpp_results = gen_dataset_samples(get_mbpp_plus(), model, tokenizer, device)

    write_jsonl("humaneval_" + get_output_name(model_id, quantize) + "" + ".jsonl", humaneval_results)
    write_jsonl("mbpp_" + get_output_name(model_id, quantize) + "" + ".jsonl", mbpp_results)

if __name__ == "__main__":
    main()