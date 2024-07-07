import re

def parse_text(text, patterns):
    
    Parse text using multiple patterns, including regular expressions.

    text: Text to be parsed.
    patterns: Dictionary of named patterns, which can be regular expressions or functions.
                     E.g., {'phones': r'\d{3}-\d{3}-\d{4}', 'custom': custom_function}
    return Dictionary with names and lists of matched groups.
    
    results = {}
    for name, pattern in patterns.items():
        if isinstance(pattern, str):
            matches = re.findall(pattern, text) # If pattern is a string, use it as a regex
        elif callable(pattern):
            matches = pattern(text) # If pattern is a function, call it with the text
        else:
            raise ValueError(f"Pattern {name} must be a regular expression or a callable function.")
        results[name] = matches
    return results

# Example usage
# def custom_function(text):
#     # Custom parsing logic here
#     return []

# text = "The phone numbers are 123-456-7890 and 987-654-3210. Emails: example@example.com, test@test.com."
# patterns = {
#     'phones': r'\d{3}-\d{3}-\d{4}',  # Pattern to match phone numbers
#     'custom': custom_function        # Custom parsing function
# }
# matches = parse_text(text, patterns)
# print(f"Extracted matches: {matches}")
