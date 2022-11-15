"""A TXT Ingestor to parse quotes from a txt file.

Takes a file path and returns a list of quotes containing QuoteModel of
quote body and author if the file can be parsed.
"""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from typing import List

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path of a file and tests if this can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('Doesnot support ingestion of this extension')

        quotes = []
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        
        return quotes