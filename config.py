from os import getenv
from dotenv import load_dotenv
load_dotenv()
MODEL_NAME = getenv("MODEL_NAME", "qwen2.5:3b")
URL = getenv("URL", "http://localhost:11434/api/chat")