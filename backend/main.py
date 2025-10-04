from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
from database import engine, Base, database, metadata
from fastapi.middleware.cors import CORSMiddleware
from routes import router as send_messages_router
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")
app.include_router(router)

# Create database tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    metadata.create_all(engine)  # Create tables on startup
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(send_messages_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))