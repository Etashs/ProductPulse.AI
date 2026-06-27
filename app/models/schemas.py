from pydantic import BaseModel


class CompareRequest(BaseModel):
    url1: str
    url2: str


class CompareResponse(BaseModel):
    status: str
    app1: dict
    app2: dict
    winner: str