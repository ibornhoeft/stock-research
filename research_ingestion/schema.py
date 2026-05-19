from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Entity:
    company_name: str
    ticker_candidates: List[str]
    mention_count: int

@dataclass
class Sentiment:
    overall: str
    by_section: Dict[str, str]

@dataclass
class Traceability:
    page_map: Dict[str, List[int]]
    raw_text_ref: str

@dataclass
class DocumentOutput:
    document_id: str
    file_name: str
    entities: List[Entity]
    signals: Dict[str, List[str]]
    sentiment: Sentiment
    themes: List[str]
    traceability: Traceability