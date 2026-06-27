import re

from google_play_scraper import app
from google_play_scraper import reviews


def extract_app_id(url: str):

    match = re.search(r"id=([A-Za-z0-9._]+)", url)

    if not match:
        raise ValueError("Invalid Google Play URL")

    return match.group(1)


def fetch_app_details(url: str):

    app_id = extract_app_id(url)

    app_info = app(
        app_id,
        lang="en",
        country="us"
    )

    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        count=100
    )

    review_list = []

    for review in result:

        review_list.append(review["content"])

    return {

        "app_name": app_info["title"],

        "developer": app_info["developer"],

        "rating": app_info["score"],

        "total_reviews": len(review_list),

        "reviews": review_list

    }