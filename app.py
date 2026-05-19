from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import sqlite3

app = FastAPI()

class Expense(BaseModel):
    name: str
    amount: float
    category: str
    month: Optional[str]= None
    year: Optional[int] = None

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
    expenses = [Expense(name=row[1], amount=row[2], category=row[3], month=row[4], year=row[5]) for row in rows]
    return {"expenses": expenses}

@app.get("/expenses_by_month/{month}")
def get_expense_by_month(month: str):
    con = sqlite3.connect("Expense.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM expense WHERE name='{month}'")
    rows = cur.fetchall()
    expenses = [Expense(name=row[1], amount=row[2], category=row[3], month=row[4], year=row[5]) for row in rows]
    return {"expenses": expenses}


@app.get("/total_expense")
def get_expense_by_month():
    con = sqlite3.connect("Expense.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM expense")
    rows = cur.fetchall()
    expenses = [Expense(name=row[1], amount=row[2], category=row[3], month=row[4], year=row[5]) for row in rows]

    for i in expenses[2]:
        total= total+i

    return {"total expenses": total}
