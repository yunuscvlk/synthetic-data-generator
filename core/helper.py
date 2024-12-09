import random

def calculate_weights(df, column_name):
    value_counts = df[column_name].value_counts(normalize=True)
    weights = {k: round(v, 1) for k, v in value_counts.items()}
    
    return weights

def weighted_choice(choices, weights):
    total = sum(weights)
    r = random.uniform(0, total)
    upto = 0

    for choice, weight in zip(choices, weights):
        if upto + weight >= r:
            return choice
        
        upto += weight

def generate_row_with_weights(content):
    rows = {}

    for _, v in content.items():
        if "time" in v:
            rows[v["description"]] = v["time"]()
        else:
            rows[v["description"]] = weighted_choice(v["answers"], v["weights"])

    return rows