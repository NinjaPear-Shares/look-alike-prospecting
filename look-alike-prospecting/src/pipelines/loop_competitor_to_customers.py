from src.clients.ninjapear import NinjaPearClient
from src.models import ProspectAccount
from src.scoring import score_account

client = NinjaPearClient()
response = client.get_customer_listing("https://stripe.com")
accounts = [
    ProspectAccount.from_customer_listing(item, source="customer_listing")
    for item in response["customers"]
]
scored_accounts = [score_account(account) for account in accounts]

if __name__ == "__main__":
    for account in scored_accounts[:3]:
        print(account.model_dump())
