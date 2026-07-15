from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
def register_user():
    return {
        "message": "User registered successfully"
    }

@router.get("/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Hari",
        "membership": "Prime"
    }