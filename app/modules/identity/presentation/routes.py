# from fastapi import APIRouter, Depends, HTTPException
# from app.modules.identity.application.commands.login_user import login
# from app.modules.identity.application.commands.register_user import register

# router = APIRouter()



# @router.post("/register")
# def register_user(username: str, password: str, email: str):
#     result = register(username, password, email)
#     if not result.success:
#         raise HTTPException(status_code=400, detail=result.error)
#     return {"message": "User created successfully"}


from fastapi import APIRouter, HTTPException
from app.modules.identity.application.commands.login_user import login
from app.modules.identity.application.commands.register_user import register
from app.modules.identity.presentation.schemas import RegisterRequest , LoginRequest

router = APIRouter()

@router.post("/login")
def login_user(req: LoginRequest):
    token = login(req.username, req.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return token

@router.post("/register")
def register_user(req: RegisterRequest):
    result = register(req.username, req.password, req.email)
    if not result.success:
        raise HTTPException(status_code=400, detail=result.error)
    return {"message": "User created successfully"}