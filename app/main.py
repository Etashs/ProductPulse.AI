from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from pydantic import BaseModel

app = FastAPI(
    title="ProductPulse AI",
    version="1.0"
)

# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")


# -------------------------
# Request Model
# -------------------------

class CompareRequest(BaseModel):

    app1_url: str

    app2_url: str


# -------------------------
# Home
# -------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# -------------------------
# Health
# -------------------------

@app.get("/health")
async def health():

    return {
        "status": "Backend Running"
    }


# -------------------------
# Compare Apps
# -------------------------

@app.post("/compare")
async def compare_apps(data: CompareRequest):

    print("App 1")

    print(data.app1_url)

    print("App 2")

    print(data.app2_url)

    return {

        "status": "success",

        "message": "Backend Connected Successfully",

        "app1": {

            "name": "Spotify",

            "sentiment": 82

        },

        "app2": {

            "name": "Apple Music",

            "sentiment": 74

        }

    }