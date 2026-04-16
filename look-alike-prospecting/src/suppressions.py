from src.models import ProspectAccount, ProspectPerson


def is_suppressed_account(account: ProspectAccount, suppression_websites: set[str]) -> bool:
    return str(account.website) in suppression_websites


def is_suppressed_person(person: ProspectPerson, suppression_emails: set[str] | None = None) -> bool:
    suppression_emails = suppression_emails or set()
    return person.work_email in suppression_emails
