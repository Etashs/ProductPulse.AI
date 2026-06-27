from google_play_scraper import app, reviews


def fetch_app_details(playstore_url):

    try:

        # Extract Package Name

        package_name = playstore_url.split("id=")[1]

    except IndexError:

        raise ValueError("Invalid Google Play Store URL")

    # Fetch App Information

    app_info = app(
        package_name,
        lang="en",
        country="in"
    )

    # Fetch Reviews

    review_list, _ = reviews(
        package_name,
        lang="en",
        country="in",
        count=100
    )

    review_text = []

    for review in review_list:

        review_text.append(review["content"])

    return {

        "package": package_name,

        "name": app_info["title"],

        "developer": app_info["developer"],

        "rating": app_info["score"],

        "installs": app_info["installs"],

        "reviews": review_text

    }