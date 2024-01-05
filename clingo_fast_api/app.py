from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from clingo import Control, Model
from typing import Iterable
from clingo_fast_api.converter import to_atoms

app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    title="Clingo-Fast-API",
    description="An API for running ASP programs.",
)

# EXCEPTION HANDLING -------------------------------------------------------------


@app.exception_handler(RequestValidationError)
async def unicorn_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=442,
        content={"Error": f"Malformed ASP program: {exc}"},
    )


# --------------------------------------------------------------------------------


# REST API -----------------------------------------------------------------------

@app.post("/answer-sets", status_code=200)
async def run(body: str = Body(..., media_type="text/plain")) -> list:
    answer_sets: Iterable[Iterable[str]] = []

    def on_model(model: Model):
        answer_sets.append(to_atoms(model))

    control: Control = Control(arguments=["-n 1000"])
    program = body

    if not program:
        raise RequestValidationError("No ASP program provided.")

    try:
        control.add("base", [], str(program))
    except RuntimeError as e:
        raise RequestValidationError(e)

    control.ground([("base", [])])
    with control.solve(on_model=on_model, async_=True) as handle:
        handle.wait()
        return answer_sets


# --------------------------------------------------------------------------------
