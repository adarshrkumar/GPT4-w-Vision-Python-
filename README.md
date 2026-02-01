# GPT4-w-Vision-Python

A Python script for analyzing images using OpenAI's GPT-4 Vision API.

## Features

- Upload and analyze images with GPT-4 Vision
- Custom text prompts for image analysis
- Base64 image encoding
- Interactive command-line interface

## Usage

1. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

2. Place images in the `uploads/` folder

3. Run the script:
   ```bash
   python main.py
   ```

4. Enter the image filename and your question about the image

## Example

```
Enter the path of the image in the uploads folder: photo.jpg
Enter the text prompt: What objects are in this image?
```

## Requirements

- Python 3.x
- OpenAI API key with GPT-4 Vision access
- `requests` library

## Dependencies

```bash
pip install requests
```

## Tech Stack

- Python
- OpenAI GPT-4 Vision API
- Poetry for dependency management
