import subprocess
import glob
import json
import ast
from ResultUtils import process_model_name

def main():
    results_plus = {}
    results_normal = {}
    files_to_evaluate = glob.glob("generated_code/*.jsonl")
    for jsonl in files_to_evaluate:
        benchmark = ""
        model_name = ""
        if "humaneval" in jsonl:
            benchmark = "humaneval"
            model_name = jsonl[len("humaneval_"):]
        elif "mbpp" in jsonl:
            benchmark = "mbpp"
            model_name = jsonl[len("mbpp_"):]
        result = subprocess.run(["evalplus.evaluate",
                                "--dataset",benchmark,
                                "--samples",jsonl], 
                        capture_output=True,
                        text=True)
        benchmark_score = result.stdout
        plus_benchmark_score = ast.literal_eval(benchmark_score.split("\n")[-2])["pass@1"]
        normal_benchmark_score = ast.literal_eval(benchmark_score.split("\n")[-4])["pass@1"]

        model_name, quant = process_model_name(model_name)

        if model_name not in results_plus:
            results_plus[model_name] = {}
            results_normal[model_name] = {}
        if benchmark not in results_plus[model_name]:
            results_plus[model_name][benchmark] = {}
            results_normal[model_name][benchmark] = {}
        
        results_plus[model_name][benchmark][quant] = plus_benchmark_score
        results_normal[model_name][benchmark][quant] = normal_benchmark_score
        print(f"Results on {benchmark} dataset for model {model_name} with quantization {quant}:")
        print(results_plus[model_name][benchmark][quant])
        print(results_normal[model_name][benchmark][quant])
    
    with open("all_benchmark_results_plus.json","w") as outfile:
        json.dump(results_plus, outfile)

    with open("all_benchmark_results_normal.json","w") as outfile:
        json.dump(results_normal, outfile)
    

if __name__ == "__main__":
    main()