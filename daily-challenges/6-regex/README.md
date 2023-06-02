# Regex pattern
- The code imports the re module, which provides functions for working with regular expressions.

- The extract_phone_numbers(string) function takes a string as input and uses a regex pattern to extract phone numbers from it. The pattern r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}" matches various phone number formats, including those with or without parentheses, with or without separators like dashes or dots. It uses the re.findall() function to find all occurrences of the pattern in the string and returns a list of phone numbers.

- The extract_email_addresses(string) function takes a string as input and uses a regex pattern to extract email addresses from it. The pattern r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" matches valid email addresses. It uses the re.findall() function to find all occurrences of the pattern in the string and returns a list of email addresses.

- The replace_email_addresses(string, replacement) function takes a string and a replacement string as input. It uses a regex pattern to find email addresses in the string and replaces them with the replacement string. The pattern and replacement are passed to the re.sub() function, which performs the substitution and returns the modified string.


<p>It calls the extract_phone_numbers(string) function and prints the extracted phone numbers.
It calls the extract_email_addresses(string) function and prints the extracted email addresses.
It calls the replace_email_addresses(string, "rickyk@gmail.com") function and prints the modified string with the email address replaced.
By running this code, you can extract phone numbers and email addresses.</p>