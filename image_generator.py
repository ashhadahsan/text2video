import requests
import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI
import os
from tqdm import tqdm
import requests
from datetime import datetime

client = OpenAI()


def resize_image(name):
    image = Image.open(name)

    # Resize the image
    resized_image = image.resize((768, 768))

    # Save the resized image
    resized_image.save(name)


timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


def generate_images(image_prompts, timestamp):
    images = []

    for prompt in tqdm(image_prompts):
        response = client.images.generate(
            prompt=prompt, n=1, size="1024x1024", model="dall-e-3"
        )

        if response.data:
            image_url = response.data[0].url
            images.append(image_url)
        else:
            print(f"Error generating image for prompt '{prompt}'")
            return []
    return images


def save_images(images, timestamp):
    with ThreadPoolExecutor(
        max_workers=5
    ) as executor:  # You can adjust max_workers as per your requirement
        futures = []
        for idx, image_url in enumerate(images):
            futures.append(
                executor.submit(
                    download_image, image_url, f"image_{timestamp}_{idx}.png"
                )
            )
        for future in tqdm(futures, desc="Downloading", total=len(futures)):
            future.result()


def download_image(url, filename):
    os.makedirs("images", exist_ok=True)
    filename = os.path.join(os.getcwd(), "images", filename)
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    resize_image(filename)
