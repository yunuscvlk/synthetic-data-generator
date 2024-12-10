from faker import Faker  # type: ignore
from .helper import *

def create_content(df, ignore_list):
    content = {}

    for idx, (q, _) in enumerate(df.dtypes.items()):
        if q in ignore_list:
            continue

        answers, weights = [], []
        results = calculate_weights(df, q)

        for a, w in results.items():
            answers.append(a)
            weights.append(w)

        if "time" in q.lower() or "zaman" in q.lower():
            continue
        
        content[f"Q{idx}"] = {
            "description": q,
            "answers": answers,
            "weights": weights,
        }
    
    return content

def generate(df, ignore_list):
    content = {}

    for i in ignore_list:
        if "time" in i.lower() or "zaman" in i.lower():
            content["Q#"] = {
                "description": i.encode("cp1252").decode("utf8"),
                "time": lambda: Faker().date_time_this_year().strftime("%Y/%m/%d %I:%M:%S %p GMT+3")
            }

    content.update(create_content(df, ignore_list))
    return content