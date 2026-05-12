from os import getenv
from dotenv import load_dotenv
from pathlib import Path    
load_dotenv()
MODEL_NAME = getenv("MODEL_NAME", "nomic-embed-text")
URL_EMBED = getenv("URL_EMBED", "http://localhost:11434/api/embeddings")
EMBED_THRESHOLD = float(getenv("EMBED_THRESHOLD", 0.8))
BASE_DIR = Path(__file__).parent
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge"
TRAVEL_AGENCY_POLICY_FILE = KNOWLEDGE_BASE_DIR / "travel_policy.txt"
MODEL_FILE_NAME=getenv("MODEL_FILE_NAME", "travel_agency_policy.joblib")
CACHE_TTL_SECONDS = int(getenv("CACHE_TTL_SECONDS", 3600))