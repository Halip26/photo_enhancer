**[![Twitter Badge](https://img.shields.io/twitter/follow/halip26?style=social)](https://twitter.com/Halip26)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/halipuddin/)
[![Medium Badge](https://img.shields.io/badge/medium-%2312100E.svg?&style=for-square&logo=medium&logoColor=white)](https://medium.com/@halip26)**

# Image UpScaling using cutout.pro API

This code helps to upscale the image using the cutout.pro API. You need to install the `tqdm` and `requests` packages before running the code. The `API_TOKEN_KEY` is stored in the `key.py` file.

## Installation

To install the required packages, run the following command in your terminal:

```bash
$pip install requests

$pip install tqdm

```

## How to Use

To run locally, run this command on your git bash:

Linux, Windows and macOS:

```bash
sudo git clone https://github.com/Halip26/image_enhancer.git
```

```bash
cd image_enhancer
```

Windows:

```bash
git clone https://github.com/Halip26/image_enhancer.git
```

```bash
cd image_enhancer
```

Run on terminal:

```bash
$python.exe .\main.py
```

## Image Enhancer API requests

A Python API wrapper for Enhance your pictures using [cutout.pro](https://www.cutout.pro/)'s [API](https://www.cutout.pro/api).

<p align="center"><img src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif" style="width:100%"  /></p>

## Usage

Before running the code, make sure you have the `API_TOKEN_KEY` stored in the `key.py` file. Then, provide the path of the image file that you want to upscale in the `upScaling` function.

```python
from tqdm import tqdm
import requests
from datetime import datetime
from key import API_TOKEN_KEY


def upScaling(img):
    response = requests.post(
        "https://www.cutout.pro/api/v1/matting2?mattingType=18",
        files={"file": open(img, "rb")},
        headers={"APIKEY": API_TOKEN_KEY},
        stream=True,  
    )

    total_length = int(response.headers.get("content-length", 0))

    progress_bar = tqdm(total=total_length, unit="iB", unit_scale=True)

    with open(
        "output/hasilnya-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "wb"
    ) as out:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:

                progress_bar.update(len(chunk))

                out.write(chunk)

    progress_bar.close()

# Provide the path of the image to upscale
upScaling(img="img/me.jpg")

```

### Features

This code provides a function called upScaling to upscale an image using the cutout.pro API. It uses the requests package to make a POST request to the API with the image file as input and the API token key stored in a key.py file. The code also uses the tqdm package to show a progress bar while the image is being upscaled. The output image is saved in the output folder with a timestamp appended to the filename. The code offers a usage example calling the upScaling function with an image file path.

---

### 🛠 &nbsp;Languages and Tools

<p>
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;

<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original.svg" title="VSCode" alt="VSCode" width="40" height="40"/>&nbsp;

</p>

---

### Contact

- 📫 How to reach me: &nbsp; [![Linkedin Badge](https://img.shields.io/badge/-Halipuddin%20Hambali-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/halipuddin/)

---
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
