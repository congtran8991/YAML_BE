from fastapi import FastAPI
from apps.user_accounts import login_view, account_view 
from apps.products import product_view

app = FastAPI()

# Add routers from all apps
app.include_router(login_view.router)
app.include_router(account_view.router)
app.include_router(product_view.router)


@app.get("/")
async def read_example():
    return {"Hello": "World"}