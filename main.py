from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import engine
from models import Base
from routers import predict


# DB 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Image Classifier API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(predict.router)

@app.get("/")
def root():
    return {"message": "AI Image Classifier API is running 🚀"}
