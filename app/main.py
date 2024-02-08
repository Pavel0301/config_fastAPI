from fastapi import FastAPI, Query
from datetime import date


app = FastAPI()


@app.get('/hotels/{location}')
def get_hotels(
    locations: str,
    date_from: date,
    date_to: date,
    has_spa: bool = Query(default=None),
    stars: int = Query(ge=1, le=5, default=None),
):
    return date_from, date_to
