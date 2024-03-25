import json
import os

def extract_solution_from_jsonl(jsonl_file):
    with open(jsonl_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            task_id = data.get('task_id', '').strip()
            solution = data.get('solution', '').strip()
            if task_id and solution:
                # Remove "<s>" from the beginning of the solution
                solution = solution.replace("<s>", "").strip()
                yield task_id, solution

def write_solution_to_file(task_id, solution, output_dir):
    file_path = os.path.join(output_dir, task_id.replace("/", os.sep) + ".py")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(solution)

def process_jsonl_files(jsonl_files, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for jsonl_file in jsonl_files:
        for task_id, solution in extract_solution_from_jsonl(jsonl_file):
            write_solution_to_file(task_id, solution, output_dir)

if __name__ == "__main__":
    jsonl_files = ["../humaneval_CodeLlama-7b-hf.jsonl"]  
    output_directory = "output_python_files" 
    process_jsonl_files(jsonl_files, output_directory)