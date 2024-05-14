from fastapi import UploadFile
from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=key)

    file_content = await file.read()
    base64_string = base64.b64encode(file_content).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_string}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    return {"response": response.choices[0].message.content}
