import requests
from datetime import datetime
from key import API_TOKEN_KEY


def upScaling(img):
    response = requests.post(
        "https://www.cutout.pro/api/v1/matting2?mattingType=18",
        files={"file": open(img, "rb")},
        headers={"APIKEY": API_TOKEN_KEY},
    )
    with open(
        "output/hasilnya-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "wb"
    ) as out:
        out.write(response.content)


upScaling(img="img/me.jpg")
