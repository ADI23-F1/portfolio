from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Portfolio Static Host")


@app.get("/")
def read_index():
    # \"\"\"Serve the HTML entry point from the repo root.\"\"\"
    index_file = BASE_DIR /"index.html"
    return FileResponse(index_file)


@app.get("{path:path}")
def read_static(path: str):
    # \"\"\"Serve any additional files alongside the HTML page.\"\"\"
    target = BASE_DIR / path
    if target.is_file():
        return FileResponse(target)
    return FileResponse(BASE_DIR / "index.html")
