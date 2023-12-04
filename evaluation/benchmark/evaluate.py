from collections import defaultdict
from pathlib import Path
from typing import Optional

from pandas import DataFrame, read_csv
from rectools import Columns
from rectools.metrics import NDCG, Precision

K = 10
FOLD_NUM = 5


def get_ml_100k_df(dataset_path: str, split: str = "train") -> Optional[DataFrame]:
    """
    Read a MovieLens 100k dataset and return a DataFrame.

    Args:
        dataset_path (str): The path to the dataset file.
        split (str, optional): Specifies whether to read 'train' or 'test' split. Default is 'train'.

    Returns:
        Optional[pd.DataFrame]: Returns a DataFrame containing the specified split of the dataset.
        Returns None if 'split' is neither 'train' nor 'test'.

    Raises:
        FileNotFoundError: If the dataset file is not found.
        ValueError: If an invalid 'split' value is provided.

    Examples:
        # Read 'train' split of the dataset
        train_data = get_ml_100k_df('path/to/train_data.csv', split='train')

        # Read 'test' split of the dataset
        test_data = get_ml_100k_df('path/to/test_data.csv', split='test')
    """
    df: Optional[DataFrame] = None

    if split == "train":
        df = read_csv(
            dataset_path,
            sep="\t",
            header=None,
            names=[Columns.User, Columns.Item, Columns.Weight, Columns.Datetime],
        )
    elif split == "test":
        df = read_csv(
            dataset_path,
            sep="\t",
            header=None,
            names=[Columns.User, Columns.Item, Columns.Weight, Columns.Datetime],
            usecols=[Columns.User, Columns.Item],
        )
    else:
        raise ValueError("Invalid split. Use 'train' or 'test'.")

    return df


model_outputs = defaultdict(list)

data_interim_dir = Path("data/interim")
items = sorted(data_interim_dir.glob("*"))

for item in items:
    model_name, _ = item.name.split(".")[0].split("_")
    model_outputs[model_name].append(read_csv(item.absolute()))
data_raw_dir = Path("data/raw/ml-100k")
test_dfs = []

for i in range(FOLD_NUM):
    test_dfs.append(get_ml_100k_df(data_raw_dir / f"u{i + 1}.test", split="test"))
precision = Precision(k=K)

for i in range(FOLD_NUM):
    print(
        f"fold={i + 1}, Acc: {precision.calc(reco=model_outputs['light-fm-wrapper-model'][i], interactions=test_dfs[i]):0.4f}"
    )
ndcg = NDCG(k=K)

for i in range(FOLD_NUM):
    print(
        f"fold={i + 1}, NDCG: {ndcg.calc(reco=model_outputs['light-fm-wrapper-model'][i], interactions=test_dfs[i]):0.4f}"
    )
