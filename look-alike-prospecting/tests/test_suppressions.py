from src.models import ProspectAccount
from src.suppressions import is_suppressed_account


def test_is_suppressed_account():
    account = ProspectAccount(name="Figma", website="https://figma.com", source="customer_listing")
    assert is_suppressed_account(account, {"https://figma.com"}) is True
