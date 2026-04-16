import json
import os
from pathlib import Path

import httpx

from src.config import EXAMPLES_DIR


class NinjaPearClient:
    def __init__(self, api_key: str | None = None, use_examples: bool = True):
        self.api_key = api_key or os.environ.get("NINJAPEAR_API_KEY", "demo-api-key")
        self.base_url = "https://nubela.co"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.use_examples = use_examples

    def _load_example(self, filename: str):
        return json.loads((Path(EXAMPLES_DIR) / filename).read_text())

    def get_customer_listing(self, website: str):
        if self.use_examples:
            return self._load_example("sample_customer_listing.json")
        r = httpx.get(
            f"{self.base_url}/api/v1/customer/listing",
            params={"website": website},
            headers=self.headers,
            timeout=100.0,
        )
        r.raise_for_status()
        return r.json()

    def get_competitor_listing(self, website: str):
        if self.use_examples:
            return self._load_example("sample_competitor_listing.json")
        r = httpx.get(
            f"{self.base_url}/api/v1/competitor/listing",
            params={"website": website},
            headers=self.headers,
            timeout=100.0,
        )
        r.raise_for_status()
        return r.json()

    def get_similar_people(self, work_email: str):
        if self.use_examples:
            return self._load_example("sample_similar_people.json")
        r = httpx.get(
            f"{self.base_url}/api/v1/employee/similar",
            params={"work_email": work_email},
            headers=self.headers,
            timeout=100.0,
        )
        r.raise_for_status()
        return r.json()

    def get_company_updates(self, website: str):
        if self.use_examples:
            return self._load_example("sample_updates.json")
        r = httpx.get(
            f"{self.base_url}/api/v1/company/updates",
            params={"website": website},
            headers=self.headers,
            timeout=100.0,
        )
        r.raise_for_status()
        return r.json()
