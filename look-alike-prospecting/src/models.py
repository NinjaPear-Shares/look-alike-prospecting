from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class SeedAccount(BaseModel):
    name: str
    website: HttpUrl
    segment: str
    source: str
    is_closed_won: bool
    arr_band: str


class SeedContact(BaseModel):
    full_name: str
    work_email: str
    company_website: HttpUrl
    role: str
    seniority: str


class ProspectAccount(BaseModel):
    name: str
    website: HttpUrl
    industry: Optional[str] = None
    source: str
    source_evidence: List[str] = []
    fit_score: float = 0.0
    relationship_score: float = 0.0
    timing_score: float = 0.0
    total_score: float = 0.0

    @classmethod
    def from_customer_listing(cls, item: dict, source: str = "customer_listing") -> "ProspectAccount":
        return cls(
            name=item["name"],
            website=item["website"],
            industry=str(item.get("industry")) if item.get("industry") is not None else None,
            source=source,
            source_evidence=[
                f"Returned by {source}",
                f"Company id: {item.get('id', 'unknown')}",
            ],
            fit_score=0.65,
            relationship_score=0.85,
            timing_score=0.25,
            total_score=0.0,
        )


class ProspectPerson(BaseModel):
    full_name: str
    work_email: str
    company_website: HttpUrl
    role: str
    source: str
    source_evidence: List[str] = []
    account_score: float = 0.0
    person_score: float = 0.0

    @classmethod
    def from_similar_person(cls, item: dict) -> "ProspectPerson":
        return cls(
            full_name=item["full_name"],
            work_email=item.get("work_email", "[email protected]"),
            company_website=item["company_website"],
            role=item["role"],
            source="similar_people",
            source_evidence=[f"Matched as similar person to {item.get('input_role', 'seed contact')}"] ,
            account_score=0.76,
            person_score=0.80,
        )


class OutreachDraft(BaseModel):
    subject: str
    body: str
    evidence: List[str]
    confidence: float
    requires_review: bool
