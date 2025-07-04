from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg/")
async def remove_bg(image: UploadFile = File(...)):
    input_dir = "input"
    output_dir = "output"
    input_path = os.path.join(input_dir, image.filename)
    output_path = os.path.join(output_dir, "result.png")

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(input_path, "wb") as f:
            shutil.copyfileobj(image.file, f)
        logging.info(f"Saved input file to {input_path}")
    except Exception as e:
        logging.error(f"Failed to save input file: {e}")
        raise HTTPException(status_code=500, detail="Failed to save uploaded file")

    try:
        logging.info(f"Background removed, saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to process image: {e}")
        raise HTTPException(status_code=500, detail="Failed to process image")

    if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
        logging.error("Output file missing or empty after processing")
        return JSONResponse(status_code=500, content={"detail": "Processing failed, output file missing"})

    return FileResponse(output_path, media_type="image/png", filename="result.png")
