from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.repositories.users import UserRepository
from src.schemas.users import UserCreate

router = APIRouter(prefix="/pages", tags=["UI"])
templates = Jinja2Templates(directory="templates")

@router.get("/users", response_class=HTMLResponse)
def get_users_page(request: Request, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    users = repo.get_all()
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@router.get("/users/create", response_class=HTMLResponse)
def get_create_user_page(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

@router.post("/users/create")
def create_user_from_page(
    first_name: str = Form(...),
    last_name: str = Form(None),
    db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    new_user = UserCreate(
        first_name=first_name,
        last_name=last_name
    )
    repo.create(new_user)
    return RedirectResponse(url="/pages/users", status_code=303)

@router.post("/users/delete/{user_id}")
def delete_user_from_page(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    repo.delete(user_id)
    return RedirectResponse(url="/pages/users", status_code=303)