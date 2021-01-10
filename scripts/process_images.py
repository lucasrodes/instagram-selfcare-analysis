"""Process images."""
import time
import os
from PIL import Image


ORIGINAL_DIR = "pics_3"
PROCESSED_DIR = "pics_3_processed"
RESIZE = (224, 224)


def main():
    files = [file for file in os.listdir(path=ORIGINAL_DIR) if file.endswith(".jpg")]
    for i, file in enumerate(files):
        img_PIL = Image.open(os.path.join(ORIGINAL_DIR, file))
        if abs(1 - img_PIL.width / img_PIL.height) < 0.15:
            img_PIL = img_PIL.resize(RESIZE)
            img_PIL.save(os.path.join(PROCESSED_DIR, file))
        if i % 100 == 0:
            print(i, end=',')


if __name__ == "__main__":
    main()