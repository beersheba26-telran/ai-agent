from config import MODEL_FILE_NAME, EMBED_THRESHOLD
import joblib
import numpy as np
from llm_embeddings import embed
from logging_config import logger
def _load(model_file_name: str) -> list[dict]:
    return joblib.load(model_file_name)
def cosine_similarity(arDoc: np.ndarray, arQuery: np.ndarray) -> float:
    dot_product = np.dot(arDoc, arQuery)
    norm_doc = np.linalg.norm(arDoc)
    norm_query = np.linalg.norm(arQuery)
    return dot_product / (norm_doc * norm_query)
def _getBestMatchDoc(model: list[dict], query_embedding: np.ndarray) -> dict:
    best_doc = None
    best_score = -1.0
    for item in model:
        score = cosine_similarity(item["embedding"], query_embedding)
        if score > best_score:
            best_score = score
            best_doc = item["text"]
    logger.debug(f"Best score: {best_score:.4f} for document: {best_doc}")        
    return best_doc if best_score > EMBED_THRESHOLD else None
def _getAnswer(model: list[dict], query: str) -> str:
    query_embedding = embed(query)
    result = _getBestMatchDoc(model, query_embedding)
    return result if result else "No relevant policy document found."
def main():
    model: list[dict] = _load(MODEL_FILE_NAME)
    print("cosole application: input a query to find the most relevant policy line, or 'exit' to quit.")
    while True:
        try:
            query = input("Enter your query: ")
            if query.lower() == "exit":
                print("Exiting the application.")
                break
            answer = _getAnswer(model, query)
            print(f"Answer: {answer}")
        except KeyboardInterrupt :
            print("\nExiting the application.")
            break   
if __name__ == "__main__":
    main()        