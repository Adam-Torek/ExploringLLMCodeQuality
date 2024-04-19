import subprocess
import glob
import json
import ast
import re

def main():
    results_plus = {}
    results_normal = {}
    files_to_evaluate = glob.glob("humaneval_*.jsonl") + glob.glob("mbpp_*.jsonl")
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

        model_name = model_name.replace("_"," ")
        model_name = model_name.replace("-", " ")
        model_name = model_name.replace(".jsonl","")
        model_name = model_name.replace("b hf","B")
        model_name = re.sub(" v[0-9].[0-9]","", model_name)
        model_name = re.sub(" V[0-9].[0-9]","", model_name)
        
        quant = ""
        if "8 bit" in model_name:
            quant = "8 bit"
            model_name = model_name.replace(" AWQ 8 bit","")
            model_name = model_name.replace(" awq 8 bit","")
        elif "4 bit" in model_name:
            quant = "4 bit"
            model_name = model_name.replace(" AWQ 4 bit","")
            model_name = model_name.replace(" awq 4 bit","")
        else:
            quant = "unquantized"

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