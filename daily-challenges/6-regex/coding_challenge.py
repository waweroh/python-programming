import re 


def extract_phone_numbers(string):
    
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    # ( - matches to parenthesis
    # \ - escape character.
    # \d - matches any digit character.
    phone_numbers = re.findall(pattern, string)
    return phone_numbers

def extract_email_addresses(string):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_addresses =re.findall(pattern, string)
    return email_addresses


string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
print(extract_phone_numbers(string))
print(extract_email_addresses(string))





# import re

# string = "Python is a popular programming language. Some people like Python, while others prefer Java."
# pattern = r"python"

# matches = re.finditer(pattern, string, flags=re.IGNORECASE)

# for match in matches:
#     print(f"Match found at position {match.start()}: {match.group()}")