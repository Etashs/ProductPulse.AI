from app.api.routes import router
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# -------------------------------
# Create FastAPI Application
# -------------------------------

app = FastAPI(
    title="ProductPulse AI",
    description="AI Powered Product Review Comparison Platform",
    version="1.0.0"
)

# -------------------------------
# Mount Static Folder
# -------------------------------

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# -------------------------------
# Configure Templates
# -------------------------------

templates = Jinja2Templates(directory="app/templates")

# -------------------------------
# Home Route
# -------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

# -------------------------------
# Health Check Route
# -------------------------------

@app.get("/health")
async def health():

    return {
        "status": "success",
        "message": "Backend Running Successfully 🚀"
    }

app.include_router(router)