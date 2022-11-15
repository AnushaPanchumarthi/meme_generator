import imp
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor

class Ingestor(IngestorInterface):
    ingestors =[DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            try:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            except:
                raise Exception("Error in Ingestion")
    
