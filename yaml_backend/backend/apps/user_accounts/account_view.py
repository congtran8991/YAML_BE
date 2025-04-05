from fastapi import APIRouter, Depends
from sqlalchemy import text, select, update, delete
from fastapi.responses import JSONResponse

from database_connection import get_db_session
from apps.user_accounts.models import UserModel
from apps.shared_utils.db_utils import DatabaseUtils
from apps.user_accounts.schema import RegisterAccountSchema, UpdateAccountSchema


from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/accounts")
async def get_all_accounts(db_session: AsyncSession = Depends(get_db_session)):
    db_utils = DatabaseUtils(db_session)

    query = select(UserModel)
    raw_data = await db_utils.get_all_records(query)
    return_data = [
        {"id": data.id, "name": data.name, "email": data.email} for data in raw_data
    ]

    return JSONResponse(
        status_code=200,
        content={"message": "Get data successfully", "data": return_data},
    )


@router.delete("/accounts/{name}")
async def delete_specific_account(
    name: str, db_session: AsyncSession = Depends(get_db_session)
):
    from apps.shared_utils.db_utils import DatabaseUtils

    db_util = DatabaseUtils(db_session)

    sql_query = select(UserModel).where(UserModel.name == name)
    if not await db_util.get_first_record(sql_query):
        return JSONResponse(
            status_code=400,
            content={"message": "Account not found"},
        )

    # sql_query = delete(UserModel).where(UserModel.name.in_(["user7","user6"]))
    sql_query = delete(UserModel).where(UserModel.name == name)
    status = await db_util.delete_record(sql_query)
    if status:
        return JSONResponse(
            status_code=200,
            content={"message": "Delete account successfully"},
        )
    else:
        return JSONResponse(
            status_code=500,
            content={"message": "Failed to delete account "},
        )


@router.post("/accounts/update")
async def update_specific_account(
    request_data: UpdateAccountSchema,
    db_session: AsyncSession = Depends(get_db_session),
):
    from apps.shared_utils.db_utils import DatabaseUtils

    db_util = DatabaseUtils(db_session)

    sql_query = select(UserModel).where(UserModel.name == request_data.name)
    if not await db_util.get_first_record(sql_query):
        return JSONResponse(
            status_code=400,
            content={"message": "Account not found"},
        )

    sql_query = (
        update(UserModel)
        .where(UserModel.name == request_data.name)
        .values(
            email=request_data.email,
            phone_number=request_data.phone_number,
            hased_password=request_data.password,
        )
    )
    status = await db_util.update_record(sql_query)
    if status:
        return JSONResponse(
            status_code=200,
            content={"message": "Update account successfully"},
        )
    else:
        return JSONResponse(
            status_code=500,
            content={"message": "Failed to update account "},
        )


@router.post("/accounts/register")
async def register_account(
    request_data: RegisterAccountSchema,
    db_session: AsyncSession = Depends(get_db_session),
):
    db_util = DatabaseUtils(db_session)

    sql_query = select(UserModel).where(UserModel.name == request_data.name)
    if await db_util.get_first_record(sql_query):
        return JSONResponse(
            status_code=400,
            content={"message": "Account already existed"},
        )

    user_data = {
        "name": request_data.name,
        "email": request_data.email,
        "hased_password": request_data.password,
        "phone_number": request_data.phone_number,
        "is_active": False,
        "role": "customer",
    }
    user_created = await db_util.create_record(table_model=UserModel, **user_data)

    if not user_created:
        return JSONResponse(
            status_code=500,
            content={"message": "Failed to create account "},
        )

    return JSONResponse(
        status_code=200,
        content={
            "message": "Created account successfully",
            "data": {"created_user_id": user_created},
        },
    )
