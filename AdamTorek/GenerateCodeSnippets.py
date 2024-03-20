from transformers import AutoTokenizer, AutoModelForCausalLM

import transformers
import torch
from evalplus.data import get_human_eval_plus, write_jsonl

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

def main():
    device = "cuda"
    model_id = "WizardLM/WizardCoder-3B-V1.0"

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16).to(device)

    samples = [
        dict(task_id=task_id, solution=generate_code(problem["prompt"], model, tokenizer, device))
        for task_id, problem in get_human_eval_plus().items()
    ]
    output_name = "samples_" + model_id.split("/")[1] + ".jsonl"
    write_jsonl(output_name, samples)


if __name__ == "__main__":
    main()