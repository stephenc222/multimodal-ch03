import re

def clean_text(text):
    """
    Remove punctuation, convert to lowercase, and strip extra whitespace.
    """
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)  # Fixed regex pattern by removing ^ from inside brackets
    # Convert to lowercase
    text = text.lower()
    # Strip extra whitespace
    text = text.strip()
    return text

# Example usage
if __name__ == "__main__":
    raw_log = "[INFO] User123: Hi! I can't login. PLease, HELP ME ASAP!!! #12345"
    cleaned_log = clean_text(raw_log)
    print("Cleaned Log:", cleaned_log)