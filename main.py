from fastapi import FastAPI, Request
from clingo import Control
from clingo import Control
from lib.converter import answer_set_to_json

app = FastAPI()
control = Control(arguments=["--opt-mode=optN"])
answer_sets = []

def on_model(model):
    global answer_sets
    answer_sets.append(answer_set_to_json(str(model)))

@app.post("/run")
async def run(request: Request):
    program = await request.body()
    program = program.decode("utf-8")

    control.add("base", [], program)
    control.ground([("base", [])])
    with control.solve(on_model=on_model, async_= True) as handle:
        handle.wait()
        print("answer sets: ", answer_sets)
        return answer_sets


    