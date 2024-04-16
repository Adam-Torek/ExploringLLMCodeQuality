import subprocess
import glob
import json
import ast

def main():
    results = {}
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
        results[benchmark + "_" + model_name] = (plus_benchmark_score, normal_benchmark_score)
        print(f"Results on {benchmark} dataset for model {model_name}:")
        print(results[benchmark + "_" + model_name])
    
    with open("all_benchmark_results.json","w") as outfile:
        json.dump(results, outfile)
    

if __name__ == "__main__":
    main()