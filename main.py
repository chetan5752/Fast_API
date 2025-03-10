from fastapi import FastAPI

app=FastAPI()

@app.get("/",description="This is my first route")
async def Data_fetch():
    return {"Message":"Successfully completed"}