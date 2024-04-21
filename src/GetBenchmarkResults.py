import subprocess
import glob
import json
import ast
from ResultUtils import get_model_name_benchmark_quant, put_score_into_dict

def main():
    results_plus = {}
    results_normal = {}
    files_to_evaluate = sorted(glob.glob("generated_code/*.jsonl"))
    for jsonl in files_to_evaluate:
        model_name, benchmark, quant = get_model_name_benchmark_quant(jsonl)
        result = subprocess.run(["evalplus.evaluate",
                                "--dataset",benchmark,
                                "--samples",jsonl], 
                        capture_output=True,
                        text=True)
        benchmark_score = result.stdout
        plus_benchmark_score = ast.literal_eval(benchmark_score.split("\n")[-2])["pass@1"]
        normal_benchmark_score = ast.literal_eval(benchmark_score.split("\n")[-4])["pass@1"]

        results_plus = put_score_into_dict(results_plus, model_name, benchmark, quant, plus_benchmark_score)
        results_normal = put_score_into_dict(results_plus, model_name, benchmark, quant, normal_benchmark_score)
    
    with open("all_benchmark_results_plus.json","w") as outfile:
        json.dump(results_plus, outfile)

    with open("all_benchmark_results_normal.json","w") as outfile:
        json.dump(results_normal, outfile)
    

if __name__ == "__main__":
    main()