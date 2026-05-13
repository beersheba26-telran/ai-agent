from config import TRAVEL_AGENCY_POLICY_FILE, MODEL_FILE_NAME
from llm_embeddings import embed
from logging_config import logger
from joblib import dump 
def _getItems() -> list[str]:
    lines = TRAVEL_AGENCY_POLICY_FILE.read_text().splitlines()
    result = [res for line in lines if (res:=line.strip())]
    logger.debug(f"Extracted {len(result)} non-empty lines from the policy file.")
    return result
def _saveModel(model:list[dict]):
    dump(model, MODEL_FILE_NAME)
    logger.info(f"Model saved to {MODEL_FILE_NAME} with {len(model)} items.")
def _createModel(items:list[str]) -> list[dict]:
    result = [{"id": i, "text": doc, "embedding": embed(doc)} for i, doc in enumerate(items)]
    logger.debug(f"Created model with {len(result)} items.")
    return result

def main():
    items:list[str] = _getItems()
    model = _createModel(items)
    _saveModel(model)

if __name__ == "__main__":
    main()