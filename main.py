from typing import Optional
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()
global_array = []


@app.get("/")
def hello():
    return {"result": "Hello World!"}

@app.get("/sum1n/{n}")
def sum1n(n:int):
    return {"result": sum(range(1, n + 1))}


@app.get("/fibo")
def fibo(n:int):
    num1 = 0
    num2 = 1
    count=0
    for i in range(1, n):
        result = num1+num2
        num1=num2
        num2=result
    return {"result": num1}

@app.post("/reverse")
def reverse(string: str = Header(None)):
    if string:
        return {"result": string[::-1]}
    else:
        raise HTTPException(status_code=400, detail="string header missing")



class Element(BaseModel):
    element: str

@app.put("/list")
def add_to_list(element: Element):
    global_array.append(element.element)
    return {"result": global_array}

@app.get("/list")
def get_list():
    return {"result": global_array}

class Expression(BaseModel):
    expr: str

@app.post("/calculator")
def calculator(expression: Expression):
    try:
        num1, operator, num2 = expression.expr.split(',')
        num1, num2 = float(num1), float(num2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise HTTPException(status_code=403, detail="zerodiv")
            result = num1 / num2
        else:
            raise HTTPException(status_code=400, detail="invalid")
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid")