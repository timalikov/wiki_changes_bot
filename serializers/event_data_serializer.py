def serialize_event_data(data: dict) -> dict:
    return {
        "title": data.get("title", ""),
        "title_url": data.get("title_url", ""),
        "user": data.get("user", ""),
        "type": data.get("type", ""),
        "comment": data.get("comment", ""),
        "language": extract_language(data.get("meta", {}).get("domain", "")),
        "timestamp": data.get("timestamp", 0)
    }

def extract_language(domain: str) -> str:
    """
    Extracts the language code from the Wikimedia domain.
    """
    if not domain:
        return "unknown"

    parts = domain.split(".") 
    if len(parts) >= 3 and parts[1] == "wikipedia":
        return parts[0]
    else:
        return "unknown"
