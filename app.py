from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Portfolio Aditya Jena")

@app.get("/")
async def read_index():
    index_file = BASE_DIR / "index.html"
    if not index_file.exists():
        raise HTTPException(status_code=404, detail="index.html not found")
    return FileResponse(str(index_file), media_type="text/html")