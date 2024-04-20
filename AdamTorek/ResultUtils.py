import re

def process_model_name(model_name):
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

    return (model_name, quant)