from fastapi import FastAPI, Form, BackgroundTasks
from openai import OpenAI
import os
from keyword_identifier import extract_image_prompts
from image_generator import generate_images, save_images
from datetime import datetime
from dotenv import load_dotenv
from datetime import datetime
from voiceover_generator import generate_voiceover, save_voiceover
from video_creator import create_video
from fastapi.responses import FileResponse
from utils import save_story, save_story_with_image_prompts


load_dotenv()
os.environ["OPENAI_API_KEy"] = os.environ.get("OPENAI_API_KEY")

client = OpenAI()

app = FastAPI()


@app.post("/generate_video")
async def gen_video(
    prompt: str = Form(None), motion: bool = Form(False), story: str = Form(None)
):
    # return {"prompt": prompt, "motion": motion, "story": story}

    image_prompts = extract_image_prompts(story)
    print("Image prompts extracted.")

    # Save the story and image prompts together
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    print(timestamp)

    # save_story(prompt, timestamp)  # save story alone for captions
    save_story_with_image_prompts(
        story, prompt, image_prompts, timestamp
    )  # Use final_story_prompt instead of story_prompt
    images = generate_images(image_prompts, timestamp=timestamp)
    print("Images generated successfully.")
    print(images)
    save_images(images, timestamp)
    # Generate the voiceover
    voiceover = generate_voiceover(story)
    if voiceover:
        print("Voiceover generated successfully.")
        save_voiceover(voiceover, timestamp)
    else:
        print("Voiceover generation failed.")

    # Create the video
    if motion == False:
        vp = create_video(images, voiceover, story, timestamp)
        print("Video created successfully.")

    return FileResponse(
        path=vp,
        media_type="video/mp4",
    )
