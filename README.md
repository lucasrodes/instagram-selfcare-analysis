# [`#selfcare`](https://www.instagram.com/explore/tags/selfcare/) 🛀

### Colour analysis of images from Instagram posts with hashtag #selfcare

<br>

This project explores high-level colour patterns present in Instagram posts with hashtag
[`#selfcare`](https://www.instagram.com/explore/tags/selfcare/). To this end, it compares pixel colour values of #selfcare-tagged images and generic images.

The code is built using Python and is distributed under [GPL-3.0 License](LICENSE).

### Content

- [1. Data](#1-data)
- [2. Method](#2-method)
- [3. Results](#3-results)
- [4. Use the code](#4-use-the-code)


## 1. Data
![](results/collage.jpg)

For this experiment, 2 datasets have been created. One containing Instagram images with hashtag #selfcare and the other
containing generic Instagram images. 

> [Read more](#prepare-the-dataset) to prepare your dataset.

### 1.1 `#selfcare` dataset
A total of 3526 images have been retrieved mostly from the following days:

- 2021-01-07
- 2021-01-08
- 2021-01-10

However, other dates are also present. Details on the date occurences can be found in [this file](results/stats_dates.csv).

### 1.2 Generic dataset
A total of 3526 images have been retrieved. They come from different hashtags: `#tbt`, `#followme`, `#repost`, `#photooftheday`,
`#picoftheday`, `#follow`, `#like4like`, `#nature`, `#instagood`, `#instadaily`, `#instagram`, `#happy`. Data was retrieved from different dats, specific date occurences can be found in [this file](results/stats_dates_arbitrary.csv).

We deemed that the images tagged with these 12 hashtags present a wide variety of imagery that may be representative of Instagram as a whole. The hashtags have been obtained from [this list of the most used Instagram hashtags](https://influencermarketinghub.com/most-popular-instagram-hashtags/).

## 2. Method

For both datasets (selfcare and generic):

* **Download images**: Images are downloaded from Instagram posts with specific hashtags using
  [`instaloader`](https://instaloader.github.io/) package.
* **Process images**: Near-squared images are resized into (100, 100) pixel images. 
* **Build collage**: Build a collage with all (100, 100) processed images. Example [here](results/collage.png).
* **Extract palette**: Finally, the colour palette is extracted from the previously generated collage, leveraging
  [`colorgram.py`](https://github.com/obskyr/colorgram.py) package.

Finally, once results for both datasets are obtained:
* **Comparison**: Palettes obtained from both datasets are compared.
## 3. Results
In the following, results obtained from both datasets are presented.
### 3.1 `#selfcare`

Find below the palette with the 10 most descriptive colours in the dataset. Note that it also illustrates the relative share of importance of each palette component along with its corresponding RGB code. The
higher the bar, the more presence it had in the dataset. 

![](results/palette_proportion_jpg.png)

The table below shows the relative importance values:

| RGB colour 	| Relative importance 	|
|-	|-	|
| (240, 232, 223) 	| 0.299 	|
| (186, 159, 134) 	| 0.170 	|
| (121, 93, 72) 	| 0.111 	|
| (37, 26, 19) 	| 0.097 	|
| (216, 226, 236) 	| 0.072 	|
| (240, 224, 231) 	| 0.064 	|
| (230, 241, 236) 	| 0.051 	|
| (21, 28, 44) 	| 0.050 	|
| (135, 165, 189) 	| 0.047 	|
| (72, 97, 124) 	| 0.038 	|

<br>

### 3.2 Generic
Likewise, the following graph shows the same results for the generic dataset. 

![](results/palette_proportion_arbitrary_jpg.png)

The table below shows the relative importance values:

|RGB colour   |Relative importance   |
|---------------|--------------------|
| (181, 157, 134) |0.169 |
| (119, 92, 72)   |0.163 |
| (237, 230, 220) |0.162 |
| (36, 25, 18)    |0.157 |
| (21, 27, 42)    |0.084 |
| (212, 223, 234) |0.063 |
| (139, 163, 184) |0.060 |
| (75, 96, 119)   |0.056 |

<br>

## 4. Use the code
The core code of the project lives in folder [scripts](scripts), where multiple scripts are found. 
### 4.1 Installation
Make sure to have [python](https://www.python.org/downloads/) installed.

```
$ pip install -r requirements.txt
```

_This project was developed using Python 3.8_

### 4.2 Prepare the dataset
#### 4.2.1 Download images
Use the script [`download_images.py`](scripts/download_images.py). By default, images are stored under `data/original`
(make sure it exists).

```
$ python scripts/download_images.py
```

#### 4.2.2 Process images
Use the script [`process_images.py`](scripts/process_images.py). By default, images are stored under `data/processed`
(make sure it exists).

```
$ python scripts/process_images.py
```

This script resizes the images to 224x224 pixels. In order to minimize the impact of resizing (it can lead to noticeable
distortions), only near-squared images have been used.

### 4.2.3 Build data collage
Use the script [`build_collage.py`](scripts/build_collage.py).

```
$ python scripts/build_collage.py
```

By default, the generted collage is stored as
[results/collage.jpg](results/collage.jpg).

### 4.2.4 Obtain palette
Use the script [`get_palette.py`](scripts/build_collage.py).

```
$ python scripts/get_palette.py
```

This will do the following (by default):
- Obtain a 10-length colour palette and store it as [`results/palette_rgb_codes.csv`](results/palette_rgb_codes.csv).
- Generate the colour palette. Saves image as [`results/palette.png`](results/palette.png)
- Generate the colour palette bar plot, illustrating presence rate. Saves image as [`results/palette_proportion.png`](results/palette_proportion.png)

### 4.3 Others

#### 4.3.1 Some stats (post's date occurence)
Use the script [`get_stats.py`](scripts/get_stats.py).

```
$ python scripts/get_stats.py
```

By default, it saves results as [`results/stats_dates.csv`](results/stats_dates.csv)
