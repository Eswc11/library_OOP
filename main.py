from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.api.routers import books, users,pages
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(books.router)
app.include_router(users.router)
app.include_router(pages.router)
@app.get("/")
def root():
    return {"message": "Library API"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)