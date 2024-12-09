import pandas as pd

from core.generator import *
from core.helper import *

def main(example_data, number_of_data):
    df = pd.read_csv(example_data)

    content = generate(df, ["Zaman damgası"])
    data = [generate_row_with_weights(content) for _ in range(number_of_data)]

    df = pd.DataFrame(data)
    df.to_csv("./datasets/synthetic_data.csv", index=False, encoding="utf-8-sig")

    print("Synthetic data was created and saved as `synthetic_data.csv`.")

if __name__ == "__main__":
    main("./datasets/example_data.csv")