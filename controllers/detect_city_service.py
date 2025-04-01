import requests


def find_city(news_text):
    # https://huggingface.co/docs/hub/security-tokens

    api_token = 'User Access Tokens'

    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    data = {
        "inputs": news_text
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english",
        headers=headers,
        json=data
    )

    entities = response.json()
    city_counts = {}

    for entity in entities:
        if entity["entity_group"] == "LOC":
            city = entity["word"]
            city_counts[city] = city_counts.get(city, 0) + 1

    total = sum(city_counts.values())
    city_probs = {city: round((count / total) * 100, 2) for city, count in city_counts.items()} if total > 0 else {}
    return {"text": news_text, "cities": city_probs}

