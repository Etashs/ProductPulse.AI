from app.services.gemini import analyze_reviews

reviews = [
    "Amazing app.",
    "Dark mode is needed.",
    "Login keeps failing."
]

print(analyze_reviews(reviews))