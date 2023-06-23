import requests
from datetime import datetime
from key import API_TOKEN_KEY
from tqdm import tqdm


def upScaling(img):
    response = requests.post(
        "https://www.cutout.pro/api/v1/matting2?mattingType=18",
        files={"file": open(img, "rb")},
        headers={"APIKEY": API_TOKEN_KEY},
        stream=True,  # Enable streaming response content
    )

    # Get response content length in bytes
    total_length = int(response.headers.get("content-length", 0))

    # Create progress bar
    progress_bar = tqdm(total=total_length, unit="iB", unit_scale=True)

    with open(
        "output/hasilnya-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "wb"
    ) as out:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                # Update progress bar
                progress_bar.update(len(chunk))

                out.write(chunk)

    # Close progress bar after download complete
    progress_bar.close()


upScaling(img="img/me.jpg")
