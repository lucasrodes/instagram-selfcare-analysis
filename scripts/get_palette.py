import os
from PIL import Image
import ast
import colorgram
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


COLLAGE_PATH = "results/collage.jpg" # input file
PALETTE_PATH = "results/palette.png" # output file
PALETTE_PROP_PATH = "results/palette_proportion.png" # output file
PALETTE_CODES_PATH = "results/palette_rgb_codes.csv" # output file
NUM_COLORS_PALETTE = 10
FORCE_REEXECUTION = False  # re-compute palette or use stored ones


def save_palete_colors(colors):
    df = pd.DataFrame([(list(c.rgb), c.proportion) for c in colors], columns=["color_rgb", "proportion"])
    df.to_csv(PALETTE_CODES_PATH, index=False)


def get_palette_and_proportion(colors):
    palette = [list(color.rgb) for color in colors]
    proportion = [color.proportion for color in colors]
    palette = np.array(palette)[np.newaxis, :, :]
    return palette, proportion


def get_palette_and_proportion_from_path():
    df = pd.read_csv(PALETTE_CODES_PATH)
    colors = df["color_rgb"].tolist()
    proportion = df["proportion"].tolist()
    palette = [ast.literal_eval(color) for color in colors]
    palette = np.array(palette)[np.newaxis, :, :]
    return palette, proportion


def generate_palette_fig(palette):
    print("> Generating palette...")
    plt.figure(figsize=(NUM_COLORS_PALETTE*10, 10))
    plt.imshow(palette)
    plt.axis('off')
    plt.savefig(PALETTE_PATH, dpi=300, format="png")


def generate_palette_bars(palette, proportion):
    print("> Generating palette with proportion img...")
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    x = np.arange(0, 10)
    ax.bar(x, proportion, color=palette[0]/255)
    # Turn off tick labels
    ax.set_yticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.tick_params(
        axis='x',      
        which='both',      
        bottom=False,
        labelbottom=True
    )
    plt.tick_params(
        axis='y',      
        which='both',   
        left=False,
        labelbottom=False
    )
    colors_ticks = [f"RGB{tuple(c)}" for c in palette[0].tolist()]
    plt.xticks(x, colors_ticks, rotation='vertical')
    plt.savefig(PALETTE_PROP_PATH, dpi=100, bbox_inches="tight", format="png")

def main():
    if FORCE_REEXECUTION or not os.path.isfile(PALETTE_CODES_PATH):
        # Load collage
        im_collage = Image.open(COLLAGE_PATH)
        # Extract colors (and save)
        colors = colorgram.extract(im_collage, NUM_COLORS_PALETTE)
        save_palete_colors(colors)
        palette, proportion = get_palette_and_proportion(colors)
    else:
        palette, proportion = get_palette_and_proportion_from_path()
    
    # Generate and save palette image
    generate_palette_fig(palette)
    generate_palette_bars(palette, proportion)

if __name__ == "__main__":
    main()