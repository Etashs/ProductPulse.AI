from urllib.parse import urlparse, parse_qs
from google_play_scraper import app, reviews


def extract_app_id(playstore_url: str):
    """
    Extract package id from Play Store URL.
    Example:
    https://play.google.com/store/apps/details?id=com.spotify.music
    ->
    com.spotify.music
    """

    parsed = urlparse(playstore_url)

    query = parse_qs(parsed.query)

    return query["id"][0]


def fetch_app_data(playstore_url: str):

    package = extract_app_id(playstore_url)

    app_info = app(
        package,
        lang="en",
        country="us"
    )

    review_data, _ = reviews(
        package,
        lang="en",
        country="us",
        count=100
    )

    review_text = []

    for r in review_data:
        review_text.append(r["content"])

    return {

        "package": package,

        "name": app_info["title"],

        "rating": app_info["score"],

        "reviews": len(review_text),

        "review_text": review_text

    }