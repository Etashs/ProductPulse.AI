from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Import Router
from app.api.compare import router as compare_router

# -------------------------
# FastAPI App
# -------------------------

app = FastAPI(
    title="ProductPulse AI",
    version="1.0.0",
    description="LLM Powered Product Intelligence Platform"
)

# -------------------------
# Static Files
# -------------------------

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# -------------------------
# Templates
# -------------------------

templates = Jinja2Templates(
    directory="app/templates"
)

# -------------------------
# Home Page
# -------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

# -------------------------
# Health Check
# -------------------------

@app.get("/health")
async def health():

    return {
        "status": "Backend Running"
    }

# -------------------------
# Register API Router
# -------------------------

app.include_router(compare_router)