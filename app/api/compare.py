from fastapi import APIRouter

from app.models.schemas import CompareRequest

from app.services.playstore import fetch_reviews

from app.services.gemini import analyze_reviews


router = APIRouter()


@router.post("/compare")

async def compare_apps(request: CompareRequest):

    reviews1 = fetch_reviews(request.url1)

    reviews2 = fetch_reviews(request.url2)

    analysis1 = analyze_reviews(reviews1)

    analysis2 = analyze_reviews(reviews2)

    return {

        "status": "success",

        "app1": analysis1,

        "app2": analysis2

    }