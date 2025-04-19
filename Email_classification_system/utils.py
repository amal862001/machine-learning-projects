import re

def find_entities(text):
    patterns = {
        'full_name': r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b',
        'email': r'\b[\w.-]+@[\w.-]+\.\w+\b',
        'phone_number': r'\b\d{10}\b',
        'dob': r'\b\d{2}/\d{2}/\d{4}\b',
        'aadhar_num': r'\b\d{12}\b',
        'credit_debit_no': r'\b\d{16}\b',
        'cvv_no': r'\b\d{3}\b',
        'expiry_no': r'\b\d{2}/\d{2}\b',
    }
    
    entities = []
    masked_text = text
    
    for entity_type, pattern in patterns.items():
        matches = re.finditer(pattern, text)
        for match in matches:
            entities.append({
                "position": [match.start(), match.end()],
                "classification": entity_type,
                "entity": match.group()
            })
            masked_text = masked_text.replace(match.group(), f'[{entity_type}]')
    
    return entities, masked_text
