#lesson 1
class MaybeParsed:
    pass

# don't touch above this line

class Parsed(MaybeParsed):
    def __init__(self, doc_name, text):
        self.doc_name = doc_name
        self.text = text

class ParseError(MaybeParsed):
    def __init__(self, doc_name, err):
        self.doc_name = doc_name
        self.err = err

#lesson 2
class Parsed:
    def __init__(self, doc_name: str, text: str) -> None:
        self.doc_name = doc_name
        self.text = text


class ParseError:
    def __init__(self, doc_name: str, err: str) -> None:
        self.doc_name = doc_name
        self.err = err


# Don't touch above this line


def parse_document(doc_name: str, content: str) -> Parsed | ParseError:
    if content:
        return Parsed(doc_name, content)
    return ParseError(doc_name, "no content")


def display_parse_result(result: Parsed | ParseError) -> str:
    if isinstance(result, Parsed):
        return f'Parsed {result.doc_name}: {len(result.text)} characters'
    return f'Failed {result.doc_name}: {result.err}'

#lesson 3
from enum import Enum

class Doctype(Enum):
    PDF = 1
    TXT = 2
    DOCX = 3
    MD = 4
    HTML = 5

#lesson 6
from enum import Enum

DocFormat = Enum("DocFormat", ["PDF", "TXT", "MD", "HTML"])

# Don't touch above this line

def convert_format(
    content: str, from_format: DocFormat, to_format: DocFormat | None
) -> str:
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace("# ", "<h1>") + "</h1>"
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace("<h1>", "# ").replace("</h1>", "")
        case _:
            raise Exception("invalid type")

        
#lesson 7
from enum import Enum
from typing import Any


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


RawCSVData = list[list[object]]
PreparedCSVData = list[list[str]]
CSVStatusResult = tuple[str, PreparedCSVData | str]

# Don't touch above this line


def get_csv_status(status: CSVExportStatus, data: Any) -> CSVStatusResult:
    match status:
        case CSVExportStatus.PENDING:
            pending_data = list(map(lambda x: list(map(str, x)), data))
            return ("Pending...", pending_data)
        case CSVExportStatus.PROCESSING:
            processing_data = "\n".join(map(lambda x: ",".join(x), data))
            return ("Processing...", processing_data)
        case CSVExportStatus.SUCCESS:
            return ('Success!', data)
        case CSVExportStatus.FAILURE:
            pending_data = list(map(lambda x: list(map(str, x)), data))
            processing_data = "\n".join(map(lambda x: ",".join(x), pending_data))
            return ('Unknown error, retrying...', processing_data)
        case _:
            raise Exception("unknown export status")