from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Incident Management System API is running!"}

@app.get("/tickets/{tickets_id}")
async def read_ticket(tickets_id: int):
    return {"tickets_id": tickets_id, "message": f"Ticket {tickets_id} details retrieved successfully."}


@app.get("/tickets")
async def search_incidents(status:str="open"):
    return {"status": status, "message": f"Incidents with status '{status}' retrieved successfully."}