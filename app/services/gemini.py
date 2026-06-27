import google.generativeai as genai

import os


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_reviews(review_list):

    prompt = f"""

You are a Product Manager.

Analyze these customer reviews.

Return ONLY JSON.

Format:

{{
"summary":"",
"positive_percent":0,
"negative_percent":0,
"pain_points":[],
"feature_requests":[],
"winner_reason":""
}}

Reviews:

{review_list}

"""

    response = model.generate_content(prompt)

    return response.text