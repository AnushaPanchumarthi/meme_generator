"""A CSV Ingestor to parse quotes from a CSV file.

Takes a file path and returns a list of quotes containing QuoteModel of
quote body and author if the file can be parsed.
"""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """CSV Ingestor Inherits from IngestorInterface class. Tests if file extension can be
    parsed and raises an exception if it cannot. Creates a random text file
    to copy text to. Splits the lines to generate a quote body and author
    required for QuoteModel class. Returns list of QuoteModels.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path of a file and tests if this can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])#Cat(row['Name'], row['Age'], row['isIndoor'])
            quotes.append(new_quote)

        return quotes
