import re

def extract_standards(texts):
    standards = []

    for text in texts:
        matches = re.findall(r'IS\s*\d+\s*:\s*\d+', text)
        standards.extend(matches)

    seen = set()
    final = []
    for s in standards:
        if s not in seen:
            final.append(s)
            seen.add(s)

    return final[:5]
