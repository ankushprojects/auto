from Tools.Copy import perform_update
from fastapi import FastAPI, BackgroundTasks
import uvicorn


app = FastAPI()

@app.get('/')
def index():
    return "SERVER UP"


@app.get("/updatenow")
async def update_server(background_tasks: BackgroundTasks):
    """
    Endpoint to trigger server update.
    """

    background_tasks.add_task(perform_update)
    
    return {"message": "Server update started"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
