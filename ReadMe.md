# Image Analysis API with FastAPI and OpenAI

## Description

This is a FastAPI application that allows users to upload an image file and receive a response from OpenAI's GPT-4 model describing the contents of the image.

## Endpoints

### GET /

Returns a simple "Hello World" message to test the API.

### POST /uploadfile/

Accepts an image file upload and returns a response from OpenAI's GPT-4 model describing the contents of the image.

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key, loaded from a `.env` file.

## Dependencies

- FastAPI
- OpenAI
- dotenv
- cors

## Usage

1. Create a `.env` file with your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`
2. Run the application with `uvicorn main:app --reload` or `fastapi dev main.py`
3. Use a tool like `curl` or a web browser to upload an image file to the `/uploadfile/` endpoint

## Example Request

```bash
curl -X POST -F "file=@/path/to/image.jpg" http://localhost:8000/uploadfile/