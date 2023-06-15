from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.on_startup()


@app.on_event("shutdown")
async def shutdown():
    await db.on_shutdown()


@app.get("/")
async def root():
    return {"message": "Hello World"}
