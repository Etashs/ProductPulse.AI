import re

from google_play_scraper import app, reviews, Sort


def extract_app_id(url: str):
    """
    Extract the application ID from a Google Play Store URL.
    Example:
    https://play.google.com/store/apps/details?id=com.spotify.music
    →
    com.spotify.music
    """

    match = re.search(r"id=([A-Za-z0-9._]+)", url)

    if not match:
        raise ValueError("Invalid Google Play Store URL")

    return match.group(1)


def fetch_app_details(url: str):

    app_id = extract_app_id(url)

    app_info = app(
        app_id,
        lang="en",
        country="us"
    )

    review_result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=100
    )

    review_list = []

    for review in review_result:

        review_list.append(review["content"])

    return {

        "app_id": app_id,

        "name": app_info["title"],

        "developer": app_info["developer"],

        "rating": app_info["score"],

        "reviews_count": len(review_list),

        "reviews": review_list

    }