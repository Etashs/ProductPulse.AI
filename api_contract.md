# ProductPulse AI API Contract

## Version

v1.0

---

# Endpoint

POST /compare

---

## Purpose

Compare two Amazon products using customer reviews and AI analysis.

---

## Request Body

Content-Type: application/json

{
    "product1_url": "https://www.amazon.in/...",
    "product2_url": "https://www.amazon.in/..."
}

---

## Success Response

Status Code

200 OK

Response

{
    "status": "success",

    "product1": {

        "name": "",

        "rating": 0,

        "reviews_analyzed": 0,

        "sentiment": {

            "positive": 0,

            "neutral": 0,

            "negative": 0

        },

        "top_pain_points": [],

        "top_features": []

    },

    "product2": {

        "name": "",

        "rating": 0,

        "reviews_analyzed": 0,

        "sentiment": {

            "positive": 0,

            "neutral": 0,

            "negative": 0

        },

        "top_pain_points": [],

        "top_features": []

    },

    "winner": {

        "product": "",

        "reason": ""

    }
}