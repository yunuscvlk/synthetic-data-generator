from faker import Faker # type: ignore
from .helper import *

def create_content(df, config):
    content = {}

    for idx, (q, _) in enumerate(df.dtypes.items(), 1):
        if any(q in v[0] for v in config["core"]["data"]["col"]["ignore_list"]):
            continue

        if any(q in v[0] for v in config["core"]["data"]["col"]["update_list"]):
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
    last_idx = 1
    content = {}

    for idx, (n, v) in enumerate(config["core"]["data"]["col"]["add_list"], last_idx):
        if any(n in v[0] for v in config["core"]["data"]["col"]["ignore_list"]):
            continue

        hash_udf = hash((n, v))
        hash_udf_str = str(hash_udf * (-1) if hash_udf < 0 else hash_udf)

        if is_valid_python_code(v.format(FUNCTION_NAME=f"udf_{hash_udf_str}")):
            exec(v.format(FUNCTION_NAME=f"udf_{hash_udf_str}"))

            content[f"Q#{idx}"] = {
                f"udf_description": n,
                f"udf_{hash_udf_str}": locals().get(f"udf_{hash_udf_str}")
            }
        else:
            content[f"Q#{idx}"] = {
                f"udf_description": n,
                f"udf_{hash_udf_str}": v
            }
        
        last_idx += idx

    for idx, (n, v) in enumerate(config["core"]["data"]["col"]["update_list"], last_idx):
        if not n in df.columns:
            continue

        if any(n in v[0] for v in config["core"]["data"]["col"]["ignore_list"]):
            continue

        hash_udf = hash((n, v))
        hash_udf_str = str(hash_udf * (-1) if hash_udf < 0 else hash_udf)

        if is_valid_python_code(v.format(FUNCTION_NAME=f"udf_{hash_udf_str}")):
            exec(v.format(FUNCTION_NAME=f"udf_{hash_udf_str}"))

            content[f"Q#{idx}"] = {
                f"udf_description": n,
                f"udf_{hash_udf_str}": locals().get(f"udf_{hash_udf_str}")
            }
        else:
            content[f"Q#{idx}"] = {
                f"udf_description": n,
                f"udf_{hash_udf_str}": v
            }

        last_idx += idx

    content.update(create_content(df, config))
    return content