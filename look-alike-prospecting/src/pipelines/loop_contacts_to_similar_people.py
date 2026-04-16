from src.clients.ninjapear import NinjaPearClient
from src.models import ProspectPerson
from src.suppressions import is_suppressed_person

client = NinjaPearClient()
customer_contact_emails = ["[email protected]"]


def save_person(prospect: ProspectPerson):
    print(prospect.model_dump())


for work_email in customer_contact_emails:
    similar_people = client.get_similar_people(work_email=work_email)
    for person in similar_people["results"]:
        prospect = ProspectPerson.from_similar_person(person)
        if not is_suppressed_person(prospect):
            save_person(prospect)
