from faker import Faker # type: ignore
from .helper import *

def create_content(df, config):
    content = {}

    for idx, (q, _) in enumerate(df.dtypes.items(), 1):
        if any(q in v.get("name") for v in config["core"]["data"]["col"]["ignore_list"].values()):
            continue

        answers, weights = [], []
        results = calculate_weights(df, q)

        for a, w in results.items():
            answers.append(a)
            weights.append(w)
        
        content[f"Q{idx}"] = {
            "description": q,
            "answers": answers,
            "weights": weights,
        }
    
    return content

def generate(df, config):
    content = {}

    for idx, (k, v) in enumerate(config["core"]["data"]["col"]["ignore_list"].items(), 1):
        if is_valid_python_code(v["value"].format(FUNCTION_NAME=f"udf_{k}")):
            exec(v["value"].format(FUNCTION_NAME=f"udf_{k}"))

            content[f"Q#{idx}"] = {
                f"udf_description": v["name"][0] if not isinstance(v["name"], str) else v["name"],
                f"udf_{k}": locals().get(f"udf_{k}")
            }
        else:
            content[f"Q#{idx}"] = {
                f"udf_description": v["name"][0] if not isinstance(v["name"], str) else v["name"],
                f"udf_{k}": v["value"]
            }

    content.update(create_content(df, config))
    return content