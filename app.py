from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil

from services.meme import generate_meme
from services.video import process_video

app = FastAPI()

# ensure folders exist
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

# serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")


# 🔹 Health check
@app.get("/api/health")
def health():
    return {"status": "ok 🚀"}


# 🔹 Meme endpoint
@app.post("/api/meme")
async def meme(text: str = Form(...), style: str = Form(...)):
    result = generate_meme(text, style)
    return JSONResponse({"caption": result})


# 🔹 Video endpoint
@app.post("/api/video")
async def video(
    file: UploadFile,
    scale: str = Form("none"),
    fps: str = Form("none")
):
    # save file
    input_path = f"input/{file.filename}"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # process video (fake for now)
    output_path = process_video(input_path, scale, fps)

    return JSONResponse({
        "message": "processed",
        "output": output_path,
        "scale": scale,
        "fps": fps
    })
