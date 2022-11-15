"""A DOCX Ingestor to parse quotes from a CSV file.

Takes a file path and returns a list of quotes containing QuoteModel of
quote body and author if the file can be parsed.
"""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from typing import List
import docx

class DocxIngestor(IngestorInterface):
    """DOCX Ingestor strategy object.

    Inherits from IngestorInterface class. Tests if file extension can be
    parsed and raises an exception if it cannot. Creates a random text
    file to copy text to. Splits the lines to generate a quote body and
    author required for QuoteModel class. Returns list of QuoteModels.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path of a file and tests if this can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes

