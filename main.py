from io import BytesIO

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from PIL import Image
import uvicorn

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])


@app.get('/welcome')
async def root():
    with open('./index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        return HTMLResponse(html, status_code=200)


@app.get("/image")
async def get_image():
    # Load image from file or database
    img = Image.open("example.jpg")

    # Convert image to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    # Return image bytes as response
    return Response(content=img_bytes.getvalue(), media_type="image/jpeg")


if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=8008)