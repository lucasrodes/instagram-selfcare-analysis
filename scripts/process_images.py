"""Process images.

Execute script from root project.
"""
import time
import os
from PIL import Image
from utils import load_files


ORIGINAL_DIR = "data/original"
PROCESSED_DIR = "data/processed"
RESIZE = (224, 224)


def process_images(input_dir, output_dir, resize=RESIZE):
    files = load_files(input_dir, format="jpg")
    for i, file in enumerate(files):
        img_PIL = Image.open(os.path.join(input_dir, file))
        if abs(1 - img_PIL.width / img_PIL.height) < 0.15:
            img_PIL = img_PIL.resize(resize)
            img_PIL.save(os.path.join(output_dir, file))
        if i % 100 == 0:
            print(i, end=',')


def main():
    process_images(ORIGINAL_DIR, PROCESSED_DIR, RESIZE)


if __name__ == "__main__":
    main()