# Synthetic Data Generator

This tool generates synthetic data using the weights of your data in CSV format. In this way, you can obtain the desired amount of synthetic data while preserving the statistical properties of the data you will use in your work.

## Installation

```bash
git clone https://github.com/yunuscvlk/synthetic-data-generator.git
cd synthetic-data-generator
pip install -r requirements.txt
```

## Requirements

- Python 3.x

## Usage

- Edit the config.yml file to set your preferences.
- Run the Synthetic Data Generator with `python main.py`

## Configuration

You can configure the generation of synthetic data according to your needs using the `config.yml` file. Below, you will find detailed explanations of the purpose of each variable.

You should definitely configure this file before generating synthetic data.

### Core Data Configuration

- **core.data.row.count**: Specifies the amount of data to be generated.

  - **Example:** `200`

- **core.data.col.ignore_list**: Specifies the columns to be ignored in the generated dataset.

  - **Example:**
    ```yaml
    - ["X4"]
    - ["X5"]
    ```

- **core.data.col.update_list**: Specifies the columns to be updated in the generated dataset.

  - **Example:**
    ```yaml
    - ["X3", "Bachelor's Degree"]
    ```

- **core.data.col.add_list**: Specifies the columns to be added to the generated dataset.

  - **Example:**
    ```yaml
    - [
        "Timestamp",
        "{FUNCTION_NAME} = lambda: Faker().date_time_this_year().strftime('%Y/%m/%d %I:%M:%S %p GMT+3')",
      ]
    ```

### Datasets Configuration

- **datasets.filepath**: The file path where your dataset is located.

  - **Example:** `./datasets`

- **datasets.example.filename**: The file name of the sample dataset.

  - **Example:** `example_data.csv`

- **datasets.synthetic.filename**: The file name of the generated dataset.

  - **Example:** `synthetic_data.csv`
