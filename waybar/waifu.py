import requests
from PIL import Image
import io

def get_img():
    with requests.Session() as session:
        with session.get("https://nekos.best/api/v2/waifu") as resp:
            data = resp.json()
            with open("1.gif", 'wb') as file:
                with session.get(data["results"][0]["url"]) as img:
                    return img.content

def show_image(img):
    with Image.open(io.BytesIO(img)) as img:
        img.show()

if __name__ == "__main__":
    show_image(get_img())