from fastapi import FastAPI
from src.api import router  

app = FastAPI(title="AI Voice Agent", version="1.0.0")
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)