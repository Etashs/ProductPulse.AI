from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class CompareRequest(BaseModel):
    url1: str
    url2: str


@router.post("/compare")
async def compare(data: CompareRequest):

    # ----------------------------
    # Dummy Response (Replace later
    # with Play Store + Gemini logic)
    # ----------------------------

    return {
        "status": "success",
        "product1": {
            "name": "Spotify: Music and Podcasts",
            "rating": 4.33,
            "reviews": 100,
            "summary": "Spotify provides an extensive music library with strong user satisfaction but users frequently complain about advertisements and occasional app crashes.",
            "pain_points": [
                "Too many ads",
                "App crashes",
                "Offline mode issues"
            ],
            "feature_requests": [
                "Better offline mode",
                "Less intrusive ads",
                "Playlist improvements"
            ]
        },
        "product2": {
            "name": "Apple Music",
            "rating": 4.61,
            "reviews": 100,
            "summary": "Apple Music is appreciated for its excellent audio quality and premium experience, but Android users report login and recommendation issues.",
            "pain_points": [
                "Login issues",
                "Poor recommendations",
                "Buffering"
            ],
            "feature_requests": [
                "Better recommendations",
                "Improved Android login",
                "New release notifications"
            ]
        },
        "winner": "Apple Music",
        "summary": "Apple Music has a slightly higher rating, while Spotify offers a larger ecosystem. The better choice depends on whether users prioritize audio quality or music discovery."
    }