from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Expense(BaseModel):
    name: str
    amount: float
    category: str
    month: str
    year: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/create_expense/")
def create_expense(expense: Expense):
    con = sqlite3.connect("Expense.db")
    cur = con.cursor()
    cur.execute("""
        INSERT INTO expense (name, amount, category) VALUES (?, ?, ?)
    """, (expense.name, expense.amount, expense.category, expense.month, expense.year))
    con.commit()
    return expense

@app.get("/all_expenses/")
def get_all_expenses():
    con = sqlite3.connect("Expense.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM expense")
    rows = cur.fetchall()
    expenses = [Expense(name=row[1], amount=row[2], category=row[3],amount=row[4],amount=row[5], ) for row in rows]
    return {"expenses": expenses}

@app.get("/expenses_by_month/")
def get_all_expenses():
    con = sqlite3.connect("Expense.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM expense")
    rows = cur.fetchall()
    expenses = [Expense(name=row[1], amount=row[2], category=row[3]) for row in rows]
    return {"expenses": expenses}

@app.get("/expenses/{expense_id}")
def read_expense(expense_id: int, q: str | None = None):
    return {"expense_id": expense_id, "q": q}