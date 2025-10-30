import spacy
from .model import classify_text

nlp = spacy.load("en_core_web_sm")

def extract_information(text):
    doc = nlp(text)
    threats = []
    threat_type = classify_text(text)
    country = "Unknown"
    industry = "Unknown"

    for ent in doc.ents:
        if ent.label_ == "GPE":
            country = ent.text

    if "financial" in text.lower():
        industry = "Financial"
    elif "tech" in text.lower():
        industry = "Technology"
    elif "gaming" in text.lower():
        industry = "Gaming"
    elif "hospital" in text.lower():
        industry = "Healthcare"

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "EVENT"]:
            threats.append({
                "name": ent.text,
                "industry": industry,
                "country": country,
                "threat_type": threat_type,
                "severity": "Unknown"
            })
    # Add rule-based severity for now
    for threat in threats:
        if "critical" in text.lower():
            threat["severity"] = "Critical"
        elif "high" in text.lower():
            threat["severity"] = "High"
        elif "medium" in text.lower():
            threat["severity"] = "Medium"
        elif "low" in text.lower():
            threat["severity"] = "Low"

    return threats
