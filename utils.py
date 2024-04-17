def save_story_with_image_prompts(story, prompt, image_prompts, timestamp):
    with open(f"story_{timestamp}.txt", "w", encoding="utf-8") as f:
        f.write(prompt + "\n" + story + "\n\nImage Prompts:\n")
        for idx, image_prompt in enumerate(image_prompts, start=1):
            f.write(f"{idx}: {image_prompt}\n")


def save_story(story, timestamp):
    file_path = f"story_{timestamp}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(story)
    return file_path  # Return the file path where the story is saved
