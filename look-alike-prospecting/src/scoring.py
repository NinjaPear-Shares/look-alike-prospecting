from src.models import ProspectAccount


def score_account(account: ProspectAccount, source: str | None = None) -> ProspectAccount:
    account.total_score = round(
        (account.fit_score * 0.40)
        + (account.relationship_score * 0.35)
        + (account.timing_score * 0.25),
        4,
    )
    if source:
        account.source = source
    return account
