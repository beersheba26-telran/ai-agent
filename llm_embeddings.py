import numpy as np
import requests

from config import URL_EMBED, MODEL_NAME
def embed(doc: str) -> np.ndarray:
    payload = {"model": MODEL_NAME, "prompt": doc}
    response = requests.post(URL_EMBED, json=payload)
    response.raise_for_status()
    return np.array(response.json()["embedding"],dtype=np.float32)