from src.models import OutreachDraft, ProspectAccount


def build_evidence_block(account: ProspectAccount, event=None):
    evidence = list(account.source_evidence)
    if event:
        evidence.append(f"Trigger: {event['title']}")
    return evidence


def draft_outreach(account: ProspectAccount, event: dict) -> OutreachDraft:
    evidence = build_evidence_block(account, event)
    return OutreachDraft(
        subject=f"Saw this at {account.name}",
        body=f"Saw the update: {event['title']}. Usually that means the team is changing packaging, priorities, or buyer motion.",
        evidence=evidence,
        confidence=0.78,
        requires_review=True,
    )
