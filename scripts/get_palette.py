import colorgram
from PIL import Image
import numpy as np


COLLAGE_PATH = "results/collage.jpg" # input file
PALETTE_PATH = "results/palette2.jpg" # output file
PALETTE_CODES_PATH = "results/palette_rgb_codes.png" # output file
NUM_COLORS_PALETTE = 10


def main():
    # Load collage
    im_collage = Image.open(COLLAGE_PATH)
    # Extract colors
    colors = colorgram.extract(im_collage, NUM_COLORS_PALETTE)
    palette = [list(color.rgb) for color in colors]
    palette = np.array(palette)[np.newaxis, :, :]
    # Save palette image
    plt.imshow(palette)
    plt.axis('off')
    plt.savefig(PALETTE_PATH, dpi=300)
    # Save color codes
    with open(PALETTE_CODES_PATH, 'w') as f:
        f.write("\n".join(palette_rgb_codes))

if __name__ == "__main__":
    main()