from src.clients.ninjapear import NinjaPearClient
from src.models import ProspectAccount
from src.outreach import draft_outreach

client = NinjaPearClient()
account = ProspectAccount(
    name="ExampleCo",
    website="https://example.com",
    industry="Software",
    source="customer_listing",
    source_evidence=["Returned in customer listing for Stripe"],
    fit_score=0.65,
    relationship_score=0.85,
    timing_score=0.25,
)


def save_draft(draft):
    print(draft.model_dump())


updates = client.get_company_updates("https://example.com")
for event in updates["results"]:
    if event["category"] in {"website update", "blog", "x"}:
        draft = draft_outreach(account, event)
        save_draft(draft)
