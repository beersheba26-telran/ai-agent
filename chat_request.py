import requests
from logging_config import logger
def chatRequest(model_name, url, messages):
    payload = {
        "model": model_name,
        "messages": messages,
        "stream": False,
        "options": {"temperature": 0.1}
    }
    logger.debug(f"Request payload: {payload}")
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    logger.debug(f"Response data: {data}")
    logger.debug(f"Response message: {data.get('message', 'No message in response')}")
    return data["message"]["content"]