# [`#selfcare`](https://www.instagram.com/explore/tags/selfcare/) 🛀

<h3>Visual analysis of images from Instagram posts with hashtag #selfcare</h3>

<br>

This project aims to analyze high-level visual patterns from Instagram posts tagged with hashtag
[`#selfcare`](https://www.instagram.com/explore/tags/selfcare/).

The code is built using Python and is distributed under [GPL-3.0 License](LICENSE).


### Content

- [Project Overview](#project-overview)
- [Data](#data)
- [Results](#results)
- [Use the code](#use-the-code)

## Project Overview
TODO

## Data
![](results/collage.jpg)

The experiments have been done using images from Instagram posts with the hashtag `#selfcare`. The images have been retrieved mostly from the following days:

- 2021-01-07
- 2021-01-08
- 2021-01-10

However, other dates are also present. Details on the date occurences can be found in [this file](results/stats_dates.csv).

The created dataset contains **3526 images**.


## Results

![](results/palette.png)
## Use the code
The core code of the project lives in folder [scripts](scripts), where multiple scripts are found. 
### Installation
Make sure to have [python](https://www.python.org/downloads/) installed.

```
$ pip install -r requirements.txt
```

_This project was developed using Python 3.8_

### Prepare the dataset
#### Download images
Use the script [`download_images.py`](scripts/download_images.py). By default, images are stored under `data/original`
(make sure it exists).

```
$ python scripts/download_images.py
```

#### Process images
Use the script [`reshape_images.py`](scripts/reshape_images.py). By default, images are stored under `data/processed`
(make sure it exists).

```
$ python scripts/reshape_images.py
```

This script resizes the images to 224x224 pixels. In order to minimize the impact of resizing (it can lead to noticeable
distortions), only near-squared images have been used.

### Build data collage
Use the script [`build_collage.py`](scripts/build_collage.py). By default, the generted collage is stored as
[results/collage.jpg](results/collage.jpg).

```
$ python scripts/build_collage.py
```

### Obtain palette
Use the script [`get_palette.py`](scripts/build_collage.py).

```
$ python scripts/get_palette.py
```