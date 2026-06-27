import os
import json

import google.generativeai as genai


# -------------------------
# Configure Gemini
# -------------------------

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


# -------------------------
# AI Review Analysis
# -------------------------

def analyze_reviews(review_list):

    # Use only the first 50 reviews to keep prompts manageable
    reviews = review_list[:50]

    review_text = "\n".join(reviews)

    prompt = f"""
You are an experienced Product Manager.

Analyze these Google Play Store reviews.

Return ONLY valid JSON.

Format:

{{
    "summary":"",

    "winner_reason":"",

    "pain_points":[
        "",
        "",
        ""
    ],

    "feature_requests":[
        "",
        "",
        ""
    ]
}}

Reviews:

{review_text}

"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown fences if Gemini returns them
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)