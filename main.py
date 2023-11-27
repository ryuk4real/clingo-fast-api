import json
from fastapi import FastAPI, Request
from clingo import Control, SolveHandle, SolveResult

app = FastAPI()
control = Control(arguments=[])

def on_model(model):
    print(model)

@app.post("/run")
async def run(request: Request):
    program = await request.body()
    program = program.decode("utf-8")

    control.add("base", [], program)
    control.ground([("base", [])])
    control.solve(on_model=on_model)
    