from fastapi import APIRouter

from app.models.schemas import CompareRequest

from app.services.playstore import fetch_app_details
from app.services.gemini import analyze_reviews

router = APIRouter()


@router.post("/compare")
async def compare_apps(request: CompareRequest):

    # -------------------------
    # Fetch Play Store Data
    # -------------------------

    app1 = fetch_app_details(request.app1_url)

    app2 = fetch_app_details(request.app2_url)

    # -------------------------
    # Gemini Analysis
    # -------------------------

    analysis1 = analyze_reviews(app1["reviews"])

    analysis2 = analyze_reviews(app2["reviews"])

    # -------------------------
    # Winner
    # -------------------------

    winner = app1["name"]

    if len(analysis2["pain_points"]) < len(analysis1["pain_points"]):
        winner = app2["name"]

    # -------------------------
    # Final Response
    # -------------------------

    return {

        "status": "success",

        "product1": {

            "name": app1["name"],

            "rating": app1["rating"],

            "reviews": app1["reviews_count"],

            "summary": analysis1["summary"],

            "pain_points": analysis1["pain_points"],

            "feature_requests": analysis1["feature_requests"]

        },

        "product2": {

            "name": app2["name"],

            "rating": app2["rating"],

            "reviews": app2["reviews_count"],

            "summary": analysis2["summary"],

            "pain_points": analysis2["pain_points"],

            "feature_requests": analysis2["feature_requests"]

        },

        "winner": winner

    }