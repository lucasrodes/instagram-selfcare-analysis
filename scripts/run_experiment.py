"""Run all steps at once."""


from download_images import download_images
from process_images import process_images
from build_collage import build_collage
from get_palette import extract_palette_proportion, generate_palette_fig, generate_palette_bars
from utils import load_images


DO_DOWNLOAD = True
DO_PROCESS = True
DO_COLLAGE = True
DO_PALETTE = True

NUM_POSTS = 750
ORIGINAL_DIR = "../data/original_arbitrary"   # "../data/original"
PROCESSED_DIR = "../data/original_arbitrary"  # "../data/processed"
COLLAGE_IM = "../results/collage_arbitrary.png" # "../results/collage.png"
PALETTE_IM = "../results/palette_arbitrary.png"  # "../results/palette.png"
PALETTE_PROPORTION_IM = "../results/palette_proportion_arbitrary.png"  # "../results/palette_proportion.png"
RESIZE = (100, 100)
TAGS = ["tbt", "followme", "repost", "photooftheday", "follow", "like4like", "nature"]  # ["selfcare"]

def run_experiment(tags, num_posts_per_tag, original_dir, processed_dir, resize=(100, 100), collage_image_path,
                    palette_image_path, palette_proportion_image_path,
                    do_download=True, do_process=True, do_collage=True, do_palette=True):
    # Download
    if do_download:
        print(">>> Downloading")
        for tag in tags:
            download_images(hashtag=tag, num_posts=num_posts_per_tag, output_dir=original_dir)
    # Process
    if do_process:
        print(">>> Process")
        process_images(original_dir, processed_dir, resize)
    # Collage
    if do_collage:
        print(">>> Build collage")
        build_collage(processed_dir, collage_image_path)
    # Palette
    if do_palette:
        print(">>> Palette")
        palette, proportion = extract_palette_proportion(collage_image_path)
        generate_palette_fig(palette, palette_image_path)
        generate_palette_bars(palette, proportion, palette_proportion_image_path)


def main():
    run_experiment(
        tags=TAGS,
        num_posts_per_tag=NUM_POSTS,
        original_dir=OUTPUT_FOLDER,
        processed_dir=PROCESSED_DIR,
        collage_image_path=COLLAGE_IM,
        palette_image_path=PALETTE_IM, 
        palette_proportion_image_path=PALETTE_PROPORTION_IM,
        do_download=DO_DOWNLOAD,
        do_process=DO_PROCESS,
        do_collage=DO_COLLAGE,
        do_palette=DO_PALETTE
    )


if __name__ == "__main__":
    main()
    