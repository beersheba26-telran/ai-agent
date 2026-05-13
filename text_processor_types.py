from text_processor_bm25 import TextProcessorBM25
from text_processor_embed import TextProcessorEmbed 
processorTypes = {
    "BM25": TextProcessorBM25.createTextProcessor,
    "EMBED": TextProcessorEmbed.createTextProcessor 
}