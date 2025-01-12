from pydantic import BaseModel
from typing import List, Optional

class Location(BaseModel):
    shelf: str
    row: int

class AdditionalInfo(BaseModel):
    publisher: str
    language: str
    page_count: int

class BookBase(BaseModel):
    title: str
    authors: List[str]
    isbn: str
    published_year: int
    category: List[str]
    availability: bool
    location: Location
    additional_info: AdditionalInfo
    cover_url: str
    online_version_url: Optional[str]

class BookUpdate(BaseModel):
    title: Optional[str]
    authors: Optional[List[str]]
    isbn: Optional[str]
    published_year: Optional[int]
    category: Optional[List[str]]
    availability: Optional[bool]
    location: Optional[Location]
    additional_info: Optional[AdditionalInfo]
    cover_url: Optional[str]
    online_version_url: Optional[str]
