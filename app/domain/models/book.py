from dataclasses import dataclass
from datetime import date
from typing import Optional
from uuid import UUID

@dataclass
class Book:
    id: UUID
    title: str
    auhor: str
    isbn: Optional[str] 
    publication_date: Optional[date] 
    summary: Optional[str]
    page_count: Optional[int]
    cover_url: Optional[str]
    owner_id: UUID