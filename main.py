from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.api.routers import books, users,pages
from src.core.database import Base,engine
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
Base.metadata.create_all(engine)
app.include_router(books.router)
app.include_router(users.router)
app.include_router(pages.router)
@app.get("/")
def root():
    return {"message": "Library API"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)