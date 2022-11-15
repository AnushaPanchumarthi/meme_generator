"""A PDF Ingestor to parse quotes from a PDF file.

Takes a file path and returns a list of quotes containing QuoteModel of
quote body and author if the file can be parsed.
"""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path of a file and tests if this can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('Doesnot support this ingestion')

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        print(f'printing to {tmp}')
        call = subprocess.call(['pdftotext', path, tmp])
        file_reference = open(tmp,'r')
        quotes = []

        for line in file_reference.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        file_reference.close()
        os.remove(tmp)
        return quotes