import ast
import types
import random

def is_valid_python_code(code):
    if not code.strip():
        return False

    if len(code.split()) == 1:
        return False

    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

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

    for v in content.values():
        if "udf_description" in v:
            value = list(v.values())[1]
            rows[v["udf_description"]] = value() if isinstance(value, types.FunctionType) else value
        else:
            rows[v["description"]] = weighted_choice(v["answers"], v["weights"])

    return rows