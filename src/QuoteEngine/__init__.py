"""Take in files containing quotes and return a list.

A class is used to represent a quote model with quote body
and author. Abstract and child classes are used to take in
quotes from different file types and select a class which
can handle the file type and returns a list of quotes.
"""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DOCxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor