from codebleu import calc_codebleu
from evalplus.data import get_mbpp_plus, get_human_eval_plus
import glob
import json
from ResultUtils import get_model_name_benchmark_quant, put_score_into_dict

def main():
    human_eval = get_human_eval_plus().items()
    mbpp = get_mbpp_plus().items()
    bleu_scores_output = {}
    res_i = 1
    for result in sorted(glob.glob("generated_code/*.jsonl")):
        model_name, benchmark, quant = get_model_name_benchmark_quant(result)

        generated_list = []

        with open(result, "r") as result_file:
            generated_list = list(result_file)
        
        generated_solutions = []
        for result_str in generated_list:
            generated_solutions.append(json.loads(result_str)["solution"].replace("<s>",""))
        
        benchmark_data = None
        if benchmark == "humaneval":
            benchmark_data = human_eval
        elif benchmark == "mbpp":
            benchmark_data = mbpp
            benchmark = "mbpp"
        
        avg_codebleu_scores = 0
        human_solutions = []
        for eval_problem in benchmark_data:
            human_solutions.append(eval_problem[1]["canonical_solution"])

        avg_codebleu_scores = calc_codebleu(human_solutions, generated_solutions, lang="python", tokenizer=None)["codebleu"]
        
        print(f"{res_i}: Average CodeBLEU score for model {model_name} on quantization {quant} for benchmark {benchmark} is {round(avg_codebleu_scores, 5)}")
        res_i += 1

        bleu_scores_output = put_score_into_dict(bleu_scores_output, model_name, benchmark, quant, avg_codebleu_scores)

    with open("codebleu_results.json","w") as outfile:
        json.dump(bleu_scores_output, outfile)
    

if __name__ == "__main__":
    main()