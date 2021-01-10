# [`#selfcare`](https://www.instagram.com/explore/tags/selfcare/) 🛀

<h3>Visual analysis of images from Instagram posts with hashtag #selfcare</h3>

<br>

This project aims to analyze high-level visual patterns from Instagram posts tagged with hashtag
[`#selfcare`](https://www.instagram.com/explore/tags/selfcare/).

The code is built using Python and is distributed under [GPL-3.0 License](LICENSE).


### Content

- [Project Overview](#project-overview)
- [Results](#results)
- [Use the code](#use-the-code)

## Project Overview
TODO

## Data
The experiments have been done using images from Instagram posts with hashtag `#selfcare`. The images have been retrieved mostly
from the following days:

- 2021-01-07
- 2021-01-08

In total, 2900 images have been used, which have been resized to 224x224 pixels. In order to minimize the impact of resizing (it can lead to noticeable distortions), only near-squared images have eenb used.

## Results
> To recreate the results obtained below, check section [Use the code](#use-the-code).

![](results/collage.jpg)
## Use the code
The core code of the project lives in folder [scripts](scripts).
### Installation
```
$ python setup.py install
```

### Prepare the dataset
#### Download images
```
$ python scripts/download_images.py
```

#### Reshape images
Next, reshape them accordingly (only nearly-squared are preserved.
```
$ python scripts/reshape_images.py
```
