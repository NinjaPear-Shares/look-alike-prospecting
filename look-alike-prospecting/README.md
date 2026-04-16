# look-alike-prospecting

A runnable starter project for agentic look alike prospecting with PydanticAI patterns and NinjaPear sample data.

Read the full article: https://nubela.co/blog/look-alike-prospecting

## What is in here

- 4 prospecting loops
- Pydantic models for accounts, people, and outreach drafts
- synthetic CSV seeds and suppression lists
- sample NinjaPear-shaped JSON responses
- small tests for scoring and suppression logic

## Run it

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
cp .env.example .env
export NINJAPEAR_API_KEY=your_key_here
python -m src.pipelines.loop_competitor_to_customers
python -m src.pipelines.loop_crm_to_competitors
python -m src.pipelines.loop_contacts_to_similar_people
python -m src.pipelines.loop_triggers_to_outreach
```

Push from the real project root. If someone clones the repo, they should see this README.md at the top level immediately.
