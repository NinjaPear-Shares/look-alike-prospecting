from src.clients.ninjapear import NinjaPearClient
from src.models import ProspectAccount
from src.scoring import score_account

client = NinjaPearClient()
seed_account_websites = ["https://stripe.com", "https://shopify.com"]


def save_candidate(scored: ProspectAccount):
    print(scored.model_dump())


for website in seed_account_websites:
    competitors = client.get_competitor_listing(website)
    for comp in competitors["competitors"]:
        account = ProspectAccount(
            name=comp["name"],
            website=comp["website"],
            industry=str(comp.get("industry")) if comp.get("industry") else None,
            source="competitor_listing",
            source_evidence=[f"competition_type={comp.get('competition_type')}", f"reason={comp.get('reason')}"] ,
            fit_score=0.70,
            relationship_score=0.72 if comp.get("competition_type") == "product_category_overlap" else 0.58,
            timing_score=0.20,
        )
        scored = score_account(account, source="competitor_listing")
        if scored.total_score >= 0.53:
            save_candidate(scored)
