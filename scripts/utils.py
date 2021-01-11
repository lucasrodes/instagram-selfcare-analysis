import os
from PIL import Image


def load_files(path, format=None):
    if format:
        files = [file for file in os.listdir(path=path)]
    else:
        files = [file for file in os.listdir(path=path) if file.endswith(f".{format}")]
    return files

def load_images(path, format="jpg"):
    files = load_files(path, format=format)
    images = [Image.open(os.path.join(path, file)) for file in files]
    return images
