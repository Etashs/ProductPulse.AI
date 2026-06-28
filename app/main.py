from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import Compare Router
from app.api.compare import router as compare_router

# ----------------------------------------
# Create FastAPI App
# ----------------------------------------

app = FastAPI(
    title="ProductPulse AI",
    description="AI Powered Product Review Comparison Platform",
    version="1.0.0"
)

# ----------------------------------------
# Register API Routes
# ----------------------------------------

app.include_router(compare_router)

# ----------------------------------------
# Static Files
# ----------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# ----------------------------------------
# Templates
# ----------------------------------------

templates = Jinja2Templates(
    directory="app/templates"
)

# ----------------------------------------
# Home Page
# ----------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

# ----------------------------------------
# Health Check
# ----------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "success",
        "message": "Backend Running Successfully 🚀"
    }