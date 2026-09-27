from pathlib import Path
import pandas as pd
from ucimlrepo import fetch_ucirepo

def download_german_credit(destination="data/raw/dataset.csv") -> Path:
    dataset = fetch_ucirepo(id=144)
    frame = dataset.data.original
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)
    return path