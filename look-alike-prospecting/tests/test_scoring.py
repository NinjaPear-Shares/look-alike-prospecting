from src.models import ProspectAccount
from src.scoring import score_account


def test_score_account():
    account = ProspectAccount(
        name="Figma",
        website="https://figma.com",
        source="customer_listing",
        fit_score=0.65,
        relationship_score=0.85,
        timing_score=0.25,
    )
    scored = score_account(account)
    assert scored.total_score == 0.6225
