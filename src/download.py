import argparse
import requests
from PIL import Image
from io import BytesIO

CHUNK_SIZE = 256

def download_image(path, size):
    num_chunks = 0
    while True:
        url = f"https://static.satisfactory-calculator.com/imgMap/realisticLayer/Stable/{size}/{num_chunks}/{num_chunks}.png"
        print(f"Testing {url}...")
        response = requests.head(url)
        if response.ok:
            num_chunks += 1
        else:
            break

    buffer_size = int((size - 2) * CHUNK_SIZE / 2)
    image_size = int(num_chunks * CHUNK_SIZE - 2 * buffer_size)
    image_output = Image.new("RGB", (image_size, image_size))
    for x in range(num_chunks):
        for y in range(num_chunks):
            print(f"Downloading {x}, {y}...")
            url = f"https://static.satisfactory-calculator.com/imgMap/realisticLayer/Stable/{size}/{x}/{y}.png"
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            image_output.paste(img, (x * CHUNK_SIZE - buffer_size, y * CHUNK_SIZE - buffer_size))

    image_output.save(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("--size", default=4, type=int)
    args = parser.parse_args()

    download_image(args.output, args.size)
