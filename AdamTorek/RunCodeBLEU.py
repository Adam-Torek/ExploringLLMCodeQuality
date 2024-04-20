from codebleu import calc_codebleu
from evalplus.data import get_mbpp_plus, get_human_eval_plus
import glob
import json
import re
from ResultUtils import process_model_name

def main():
    human_eval = get_human_eval_plus().items()
    mbpp = get_mbpp_plus().items()
    for result in glob.glob("generated_code/*.jsonl"):
        generated_list = []

        with open(result, "r") as result_file:
            generated_list = list(result_file)
        
        generated_solutions = []
        for result_str in generated_list:
            generated_solutions.append(json.loads(result_str))
        
        benchmark = None
        if "humaneval" in result:
            benchmark = human_eval
        elif mbpp in "result":
            benchmark = mbpp

        i = 0
        avg_codebleu_scores = 0
        for eval_problem in benchmark:
            human_solution = eval_problem[1]["canonical_solution"]
            generated_solution = generated_solutions[i]["solution"]
            scores = calc_codebleu([human_solution], [generated_solution], lang="python", tokenizer=None)
            avg_codebleu_scores += scores["codebleu"]
            i += 1

        avg_codebleu_scores = avg_codebleu_scores / i
        print(avg_codebleu_scores)

        model_name, quant = process_model_name(result)
    pass

if __name__ == "__main__":
    main()