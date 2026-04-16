def summarize_research(item: dict) -> list[str]:
    return [f"source={item.get('source', 'unknown')}", "keep evidence attached"]
