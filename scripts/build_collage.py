"""Execute script from root project."""
from PIL import Image
import os
import numpy as np


PROCESSED_DIR = "data/processed/"
COLLAGE_IM = "results/collage.jpg"


class Collage:
    
    def __init__(self, images, im_size=100, ratio=2):
        """Build collage from images."""
        self.images = images
        self.im_size = im_size
        self.num_rows, self.num_cols = self.get_collage_size(ratio)
        self.collage_im = None
        
        print(f"Collage size: {self.im_size*self.num_rows}x{self.im_size*self.num_cols}")
        
    
    def get_collage_size(self, ratio):
        num_rows = int(np.floor((len(self.images)/ratio)**.5))
        num_cols = int(ratio*num_rows)
        return num_rows, num_cols

    def build(self):
        collage_im = Image.new('RGB', (self.num_cols*self.im_size, self.num_rows*self.im_size))
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                idx = int(i * self.num_rows + j)
                im = self.images[idx].resize((self.im_size, self.im_size))
                collage_im.paste(im, (i*100, j*100))
        self.collage_im = collage_im

    def save(self, output_filename):
        if self.collage_im:
            with open(output_filename, 'w') as f:
                self.collage_im.save(f)
            print(f"Image saved at {output_filename}")


def main():
    # Load images
    files = [file for file in os.listdir(path=PROCESSED_DIR) if file.endswith(".jpg")]
    images = [Image.open(os.path.join(PROCESSED_DIR, file)) for file in files]
    # Build and save collage
    collage = Collage(images)
    collage.build()
    collage.save(COLLAGE_IM)


if __name__ == "__main__":
    main()