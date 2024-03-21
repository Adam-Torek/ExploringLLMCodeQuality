from transformers import AutoTokenizer, AutoModelForCausalLM

import transformers
import torch
from evalplus.data import get_mbpp_plus, get_human_eval_plus, write_jsonl

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
    device = "cuda"
    model_id = "bigcode/starcoder2-7b"

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16).to(device)

    humaneval_results = gen_dataset_samples(get_human_eval_plus(), model, tokenizer, device)
    mbpp_results = gen_dataset_samples(get_mbpp_plus(), model, tokenizer, device)

    write_jsonl("humaneval_" + model_id.split("/")[1] + "" + ".jsonl", humaneval_results)
    write_jsonl("mbpp_" + model_id.split("/")[1] + "" + ".jsonl", mbpp_results)

if __name__ == "__main__":
    main()