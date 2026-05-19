from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

con = sqlite3.connect("Expense.db")
app = FastAPI()

cur = con.cursor()

class Expense(BaseModel):
    name: str
    amount: float
    category: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create_expense/")
def create_expense(expense: Expense):
    return expense

@app.get("/all_expenses/")
def get_all_expenses(response_model=list[Expense]):
    return {"expenses": []}

@app.get("/expenses/{expense_id}")
def read_expense(expense_id: int, q: str | None = None):
    return {"expense_id": expense_id, "q": q}