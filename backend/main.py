from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title="Choose Yor Own Adventure API",
    description="An API to create or generate new stories of your choice.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

#  CORSMiddleware - allow all origins
#  Stands for Cross-Origin Resource Sharing Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn is webserver to run FastAPI applications
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)