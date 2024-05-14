# Image Analysis API with FastAPI and OpenAI

## Description

This is a FastAPI application that allows users to upload an image file and receive a response from OpenAI's GPT-4 model describing the contents of the image. This is a FastAPI application that allows users to upload an image file and receive a response from OpenAI's GPT-4 model describing the contents of the image. The `file-uploader` folder contains a react application which you can build and run locally along with the `main.py` which happens to be the server.

```bash
cd file-uploader
npm install
npm start
```

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
