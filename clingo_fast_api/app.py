from fastapi import FastAPI, Body, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from clingo import Control  
from clingo_fast_api.converter import answer_set_to_json

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
answer_sets = None

def on_model(model):
    answer_sets.append(answer_set_to_json(str(model)))

# --------------------------------------------------------------------------------




# REST API -----------------------------------------------------------------------

@app.post("/answer-sets", status_code=200, response_model=list, )
async def run(body: str = Body(..., media_type='text/plain')) -> dict:

    global answer_sets
    answer_sets = []
    program = body

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