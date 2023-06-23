[![Twitter Badge](https://img.shields.io/twitter/follow/halip26?style=social)](https://twitter.com/Halip26)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/halipuddin/)
[![Medium Badge](https://img.shields.io/badge/medium-%2312100E.svg?&style=for-square&logo=medium&logoColor=white)](https://medium.com/@halip26)

In this project Edit background color written in python, as you’ve seen in the preview image, users can change background color in seconds powered by Artificial Intelligence that already provided by [remove.bg](https://www.remove.bg) and you just need to call & use it thorough API (Application Programming Interface) that provided here [API](https://www.remove.bg/api).

<p align="center"><img src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif" style="width:100%"  /></p>

---
### 💻 &nbsp;Preview :
<p align="center">Before</p>
<p align="center"><img src="images/preview1.png" style="width:100%" /></p>
<p align="center">After</p>
<p align="center"><img src="images/preview2.png" style="width:100%" /></p>

- 📫 How to reach me: &nbsp; [![Linkedin Badge](https://img.shields.io/badge/-Halipuddin%20Hambali-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/halipuddin/)

---

### 🛠 &nbsp;Languages and Tools :

<p> 
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;

<img src="https://github.com/devicons/devicon/blob/master/icons/vscode/vscode-original.svg" title="VSCode" alt="VSCode" width="40" height="40"/>&nbsp;

</p>

---
# remove-bg
A Python API wrapper for removing backgrounds from picture using [remove.bg](https://www.remove.bg)'s [API](https://www.remove.bg/api).

# Run Locally

To run **Techx** locally, run this command on your git bash:

Linux and macOS:

```bash
sudo git clone https://github.com/Halip26/edit_bg.git
```
```bash
cd edit_bg
```

Windows:

```bash
git clone https://github.com/Halip26/edit_bg.git
```
```bash
cd edit_bg
```
# Installation
`pip install requests`

# Before run, set the dependencies first:
```python
#this should be written on "edit_bg.py"
from api import API_TOKEN_KEY

#create a new file with name "api.py" 
#then write these code 👇

API_TOKEN_KEY = 'YOUR_API_TOKEN_KEY'

#* Create API_TOKEN_KEY from here https://www.remove.bg/dashboard#api-key

#copy your photos that you want to change the bg color 
#then, change the path name with your photos on line 22 at "edit_bg.py"

edit_bg(img='images/your-photos.png', bg_color='0000FF')

#and, that's it.

#Warm regards, Halipuddin 😎

```

# Run on terminal
`python edit_bg.py` 

# Usage
## `remove_background_from_img_file`

Removes the background given an image file.

| Parameter     | Default Value | Description   |
| ------------- | ------------- | ------------- |
| img_file_path | req. param    | path to the source image file |
| size          | `'regular'`   | size of the output image (`'auto'` = highest available resolution, `'preview'`|`'small'`|`'regular'` = 0.25 MP, `'medium'` = 1.5 MP, `'hd'` = 4 MP, `'full'`|`'4k'` = original size) |
| type          | `'auto'`      | foreground object (`'auto'` = autodetect, `'person'`, `'product'`, `'car'`) |
| type_level    | `'none'`      | classification level of the foreground object (`'none'` = no classification, `'1'` = coarse classification (e.g. `'car'`), `'2'` = specific classification (e.g. `'car_interior'`), `'latest'` = latest classification) |
| format        | `'auto'`      | image format (`'auto'` = autodetect, `'png'`, `'jpg'`, `'zip'`) |
| roi       | `'0 0 100% 100%'` | region of interest, where to look for foreground object (x1, y1, x2, y2) in px or relative (%) |
| crop          | `None`        | px or relative, single val = all sides, two vals = top/bottom, left/right, four vals = top, right, bottom, left |
| scale         | `'original'`  | image scale relative to the total image size |
| position      | `'original'`  | `'center'`, `'original'`, single val = horizontal and vertical, two vals = horizontal, vertical |
| channels      | `'rgba'`      | request the finalized image (`'rgba'`) or an alpha mask (`'alpha'`) |
| shadow        | `False`       | whether to add an artificial shadow (some types aren't supported) |
| semitransparency | `True`     | semitransparency for windows or glass objects (some types aren't supported) |
| bg            | `None`        | background (`None` = no background, path, url, color hex code (e.g. `'81d4fa'`, `'fff'`), color name (e.g. `'green'`)) |
| bg_type       | `None`        | background type (`None` = no background, `'path'`, `'url'`, `'color'`) |
| new_file_name | `'no-bg.png'` | file name of the result image |

---
### 📑 &nbsp;License:

MIT License

Copyright (c) 2023 Halip26

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
