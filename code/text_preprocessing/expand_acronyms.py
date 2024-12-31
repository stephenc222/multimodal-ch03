import json
import re

def load_acronyms(config_path):
    """
    Load acronym definitions from a JSON file.
    """
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)

def expand_acronyms(text, acronyms):
    """
    Replace known acronyms in text with their expanded forms.
    """
    for acronym, full_form in acronyms.items():
        # \b for word boundary, to match exact acronyms
        text = re.sub(r'\b' + acronym + r'\b', full_form, text)
    return text

# Example usage
if __name__ == "__main__":
    # Suppose acronyms_config.json is located in data/ (or wherever you keep configs)
    acronyms_dict = load_acronyms("data/acronyms_config.json")
    sample_log = "The CSR mentioned in the FAQ that ETA is 2 hours."
    expanded_log = expand_acronyms(sample_log, acronyms_dict)
    print("Expanded Text:", expanded_log) 