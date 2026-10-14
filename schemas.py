from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal
#--------TicketModels

class TicketCreate(BaseModel):
    title: str = Field(..., example="Issue with login",min_length=3,max_length=100)
    description: str = Field(..., example="Unable to login with correct credentials.")
    priority: Literal["low", "medium", "high","critical"] = Field(..., example="high")
    status: Literal["open", "in_progress", "closed"] = Field(default="open", example="open")
    created_at: datetime = Field(default_factory=datetime.utcnow, example="2024-06-01T12:00:00Z")


class Ticket(TicketCreate):
    id: int
    status:str="open"
    created_at: datetime


#------------------------------user models--------------------------------
class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserPublic(BaseModel):
    id:int
    name:str
    email:str