from fastapi import FastAPI

app = FastAPI(
    title="Coffee POS API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "FastAPI running"
    }