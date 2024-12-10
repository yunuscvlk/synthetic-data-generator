import yaml # type: ignore
import pandas as pd

from core.generator import *
from core.helper import *

def main(config):
    example_filename = config["datasets"]["example"]["filename"]
    synthetic_filename = config["datasets"]["synthetic"]["filename"]

    example_filepath = f"./datasets/{example_filename}"
    synthetic_filepath = f"./datasets/{synthetic_filename}"

    df = pd.read_csv(example_filepath)

    content = generate(df, config["generate"]["ignore_list"])
    data = [generate_row_with_weights(content) for _ in range(config["generate"]["number_of_data"])]

    df = pd.DataFrame(data)
    df.to_csv(synthetic_filepath, index=False, encoding="utf-8-sig")

    print(f"Synthetic data was created and saved as `{synthetic_filepath}`.")

if __name__ == "__main__":
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)

    main(config)