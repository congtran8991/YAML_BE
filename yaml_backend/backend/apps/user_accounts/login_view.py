from fastapi import APIRouter
from apps.user_accounts.models import UserModel

router = APIRouter()

@router.get("/accounts/login_test")
async def register_test():
    return {"Hello Login"}