import re

def get_model_name_benchmark_quant(input_str):
    input_str = input_str.split("/")[1]
    model_name = ""
    if "humaneval" in input_str:
        benchmark = "humaneval"
        model_name = input_str[len("humaneval_"):]
    elif "mbpp" in input_str:
        benchmark = "mbpp"
        model_name = input_str[len("mbpp_"):]
    model_name = model_name.replace("_"," ")
    model_name = model_name.replace("-", " ")
    model_name = model_name.replace(".jsonl","")
    model_name = model_name.replace("b hf","B")
    model_name = re.sub(" v[0-9].[0-9]","", model_name)
    model_name = re.sub(" V[0-9].[0-9]","", model_name)
    
    quant = ""
    if "8 bit" in model_name or "8_bit" in model_name:
        quant = "8 bit"
        model_name = model_name.replace(" AWQ 8 bit","")
        model_name = model_name.replace(" awq 8 bit","")
        model_name = model_name.replace(" 8 bit", "")
    elif "4_bit" in model_name or "4 bit" in model_name:
        quant = "4 bit"
        model_name = model_name.replace(" AWQ 4 bit","")
        model_name = model_name.replace(" awq 4 bit","")
        model_name = model_name.replace(" 4 bit", "")
    else:
        quant = "unquantized"

    return (model_name, benchmark, quant)

def put_score_into_dict(dictionary, model_name, benchmark, quant, score, use_plus=False):

    if use_plus:
        benchmark = benchmark + " Plus"

    if model_name not in dictionary:
        dictionary[model_name] = {}
    if benchmark not in dictionary[model_name]:
        dictionary[model_name][benchmark] = {}

    dictionary[model_name][benchmark][quant] = score

    return dictionary
