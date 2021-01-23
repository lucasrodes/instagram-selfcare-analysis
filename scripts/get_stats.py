import os
from PIL import Image
import pandas as pd
from datetime import datetime


PROCESSED_DIR = "../data/processed_arbitrary/"  # input
STATS_DATE_FILE = "../results/stats_dates_arbitrary.csv"  # output


def name2date(name):
    return datetime.strptime("".join(name.split('_')[1:3]), "%Y%m%d%H%M%S").date()


def main():
    # Load images
    files = [file for file in os.listdir(path=PROCESSED_DIR) if file.endswith(".jpg")]
    images = [Image.open(os.path.join(PROCESSED_DIR, file)) for file in files]
    # Build table with date occurrences
    dates = [name2date(file) for file in files]
    df = pd.DataFrame(pd.value_counts(dates).sort_index(ascending=False), columns=["number_images"])
    df.index.name = "date"
    df.to_csv(STATS_DATE_FILE)


if __name__ == "__main__":
    main()