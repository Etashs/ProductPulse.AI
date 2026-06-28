import os
import json
import google.generativeai as genai

# Configure Gemini
print("GEMINI_API_KEY =", repr(os.getenv("GEMINI_API_KEY")))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_products(product1, product2):

    reviews1 = "\n".join(product1["review_text"][:50])
    reviews2 = "\n".join(product2["review_text"][:50])

    prompt = f"""
You are an expert Product Analyst.

Compare these two Google Play Store applications.

Application 1
Name: {product1['name']}
Rating: {product1['rating']}

Reviews:
{reviews1}

----------------------------------------

Application 2
Name: {product2['name']}
Rating: {product2['rating']}

Reviews:
{reviews2}

----------------------------------------

Return ONLY valid JSON.

Format:

{{
"product1": {{
"name":"",
"rating":0,
"reviews":0,
"summary":"",
"pain_points":["","",""],
"feature_requests":["","",""]
}},
"product2": {{
"name":"",
"rating":0,
"reviews":0,
"summary":"",
"pain_points":["","",""],
"feature_requests":["","",""]
}},
"winner":""
}}
"""

    response = model.generate_content(prompt)

    text = response.text

    text = text.replace("```json", "").replace("```", "").strip()

    result = json.loads(text)

    result["status"] = "success"

    result["product1"]["reviews"] = product1["reviews"]
    result["product2"]["reviews"] = product2["reviews"]

    return result