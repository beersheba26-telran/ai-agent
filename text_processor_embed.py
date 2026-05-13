from os import getenv
import requests
import numpy as np  
from config import EMBED_MODEL_NAME, EMBED_URL, EMBED_THRESHOLD, MODEL_FILE_NAME
from text_prcessor import TextProcessor
import joblib
from rank_bm25 import BM25Okapi
from logging_config import logger   
class TextProcessorEmbed(TextProcessor):
    def __init__(self,*,text="",file="",threshold=1):
        super().__init__(text="", file=file)
        self.threshold = threshold
    def _getItems(self, lines) -> list[str]:
        result = [res for line in lines if (res:=line.strip())]
        logger.debug(f"Extracted {len(result)} non-empty lines from the policy file.")
        return result
    def _embed(self, doc: str) -> np.ndarray:
        payload = {"model": EMBED_MODEL_NAME, "prompt": doc}
        logger.debug(f"Payload for embedding: {payload}")
        logger.debug(f"Sending embedding request to {EMBED_URL} ")
        response = requests.post(EMBED_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Received embedding response: {data.get('embedding', [])[:5]}...")  # Log only the first 5 values for brevity
        if "embedding" not in data:
            logger.error(f"Embedding response does not contain 'embedding' key: {data}")
            raise ValueError("Invalid embedding response")  
        return np.array(data["embedding"],dtype=np.float32)
    def _createModel(self, items:list[str]) -> list[dict]:
        result = [{"id": i, "text": doc, "embedding": self._embed(doc)} for i, doc in enumerate(items)]
        logger.debug(f"Created model with {len(result)} items.")
        return result  
    def _cosine_similarity(self, arDoc: np.ndarray, arQuery: np.ndarray) -> float:
        dot_product = np.dot(arDoc, arQuery)
        norm_doc = np.linalg.norm(arDoc)
        norm_query = np.linalg.norm(arQuery)
        return dot_product / (norm_doc * norm_query)    
    def create_model(self,text):
        cleaned_text = self._getItems(text.splitlines())
        self.model = self._createModel(cleaned_text)
        logger.debug(f"Created EMBED model with {len(self.model)} sentences.")
        
    def load_model(self,file):   
        self.model = joblib.load(file)
        logger.debug(f"Loaded EMBED model from {file} with {len(self.model)} sentences.")
    def save_model(self,file):
        joblib.dump(self.model, file) 
        logger.debug(f"Saved EMBED model to {file} with {len(self.model)} sentences.")
    def get_answer(self, query):  
        query_embedding = self._embed(query)
        best_doc = None
        best_score = -1.0
        for item in self.model:
            score = self._cosine_similarity(item["embedding"], query_embedding)
            if score > best_score:
                best_score = score
                best_doc = item["text"]
        logger.debug(f"Best score: {best_score:.4f} for document: {best_doc}")        
        return best_doc if best_score >= self.threshold else None   
    @staticmethod
    def createTextProcessor():
        '''Factory method to create a TextProcessorEmbed instance based on environment variable.
        '''
        fileName = MODEL_FILE_NAME
        textProcessor = TextProcessorEmbed(file=fileName, threshold=EMBED_THRESHOLD)
        return textProcessor