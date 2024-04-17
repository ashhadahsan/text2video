# Text-to-Video Generation API

This API provides a seamless solution for generating videos from text inputs. It utilizes OpenAI's DALL-E for image generation, OpenAI's ChatGPT for story writing, and ElevenLabs for voice-over. By integrating these powerful tools, it enables users to convert textual descriptions into engaging video content.

## Features

- **Text-to-Video Conversion:** Transform text descriptions into dynamic video content.
- **Story Generation:** Utilize OpenAI's ChatGPT to generate compelling narratives based on input text.
- **Image Generation:** Employ OpenAI's DALL-E to create relevant images corresponding to the text.
- **Voice-Over:** Enhance videos with professional voice narration using ElevenLabs' voice-over technology.
- **FastAPI Framework:** Utilize FastAPI for efficient and high-performance API development.
- **Docker Support:** Easily deploy the API using Docker for seamless containerization.

## Requirements

- OpenAI API Key for DALL-E and ChatGPT.
- ElevenLabs API Key for voice-over functionality.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ashhadahsan/text2video.git
   ```

2. Navigate to the project directory:

   ```bash
   cd text2video
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API keys:

   - Obtain API keys from OpenAI for DALL-E and ChatGPT.
   - Obtain an API key from ElevenLabs for voice-over functionality.
   - Set these API keys as environment variables or configure them in the appropriate files.

5. Run the application:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

6. Access the API at `http://localhost:8000` in your browser or via API clients.

## Docker Deployment

To deploy using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t text-to-video-api .
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 8000:8000 text-to-video-api
   ```

3. Access the API at `http://localhost:8000` in your browser or via API clients.

Adjust the parameters according to your requirements, and handle the response accordingly.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the [MIT License](LICENSE).
