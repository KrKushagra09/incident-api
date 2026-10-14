from fastapi import FastAPI
from datetime import datetime
from schemas import TicketCreate, Ticket, UserCreate, UserPublic
app=FastAPI()
#in memory storage and counter
tickets= []
ticket_id_cntr=1
@app.get("/")
async def read_root():
    return {"message": "Incident Management System API is running!"}

@app.get("/tickets/{tickets_id}")
async def read_ticket(tickets_id: int):
    return {"tickets_id": tickets_id, "message": f"Ticket {tickets_id} details retrieved successfully."}


@app.get("/tickets")
async def search_incidents(status:str="open"):
    return {"status": status, "message": f"Incidents with status '{status}' retrieved successfully."}

@app.post("/tickets",response_model=Ticket,status_code=201)
def create_ticket(ticket: TicketCreate):
    global ticket_id_cntr
    #create the full ticket object with system generated fields
    new_ticket=Ticket(id=ticket_id_cntr,
    title=ticket.title,
    description=ticket.description,
    priority=ticket.priority,
    status=ticket.status,
    created_at=ticket.created_at
    )
    tickets.append(new_ticket)
    ticket_id_cntr += 1
    return new_ticket

@app.get("/ticket",response_model=list[Ticket])
def list_tickets():
    return tickets