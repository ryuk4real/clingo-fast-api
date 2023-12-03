from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from clingo import Control
from lib.converter import answer_set_to_json

app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs", redoc_url="/api/redoc",
    title="Clingo-Fast-API",
    description="An API for running ASP programs.")

# EXCEPTION HANDLING -------------------------------------------------------------

@app.exception_handler(RequestValidationError)
async def unicorn_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=442,
        content={"Error": f"Malformed ASP program: {exc}"},
    )

# --------------------------------------------------------------------------------




# clingo-api ---------------------------------------------------------------------

control = Control(arguments=["--opt-mode=optN"])
answer_sets = []

def on_model(model):
    global answer_sets
    answer_sets.append(answer_set_to_json(str(model)))

# --------------------------------------------------------------------------------




# REST API -----------------------------------------------------------------------

@app.post("/answer-sets", status_code=200, response_model=list)
async def run(request: Request) -> dict:

    program = await request.body()

    if not program:
        raise RequestValidationError("No ASP program provided.")

    program = program.decode("utf-8")

    try:
       control.add("base", [], program)
    except RuntimeError as e:
        raise RequestValidationError(e)
    
    control.ground([("base", [])])
    with control.solve(on_model=on_model, async_= True) as handle:
        handle.wait()
        return answer_sets

# --------------------------------------------------------------------------------