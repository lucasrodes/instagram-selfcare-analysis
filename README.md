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
