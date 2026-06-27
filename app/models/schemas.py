from pydantic import BaseModel


class CompareRequest(BaseModel):

    app1_url: str

    app2_url: str