# Hojaleaks webscraping 
The following code scrapes "https://hojaleaks.com/".It imports BeautifulSoup library for navigating, searching,modifying a parse tree in HTML, XML. Request for making HTTP requests and CSV for storing data.

Specifying the URL:
- The URL of the webpage to be scraped is assigned to the url variable.

Sending HTTP Request and Parsing the HTML:
- The requests.get() method is used to send an HTTP GET request to the specified URL and retrieve the webpage content.
- The HTML content is passed to BeautifulSoup along with the "html.parser" to create a BeautifulSoup object named doc. This object represents the parsed HTML document.

Extracting Headings and Summaries:
- The find_all() method of the doc object is used to find all the "h1" tags, which represent the headings on the webpage. The extracted headings are stored in the headings list.
- Similarly, the find_all() method is used to find all "p" tags with the class "css-ko0c54", which represent the summaries on the webpage. The extracted summaries are stored in the summaries list.

Printing Headings and Summaries:
- The code then loops over the headings list and prints each heading text using heading.text.
- Similarly, it loops over the summaries list and prints each summary text using summary.text.

Writing Extracted Data to a CSV File:
-The code opens a CSV file named "data.csv" in write mode using the open() function with the 'w' flag.
-It creates a csv.writer object named writer to write data to the CSV file.
-The first row of the CSV file is written with the column names 'Heading' and 'Summary' using writer.writerow(['Heading', 'Summary']).
-Finally, it loops over the headings and summaries lists simultaneously using zip(), writes each heading and its corresponding summary to a new row in the CSV file using writer.writerow([heading.text, summary.text]).