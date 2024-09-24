import requests

api_key = '186ecaf4a75543dd9b045964c5a6abde'
url = 'https://newsapi.org/v2/everything?q=tesla&' \
      'from=2024-08-24&sortBy=publishedAt&apiKey=' \
      '186ecaf4a75543dd9b045964c5a6abde'
#make request
request = requests.get(url)

#get a dictionary with data
content = request.json()

# Access the articles, titles and descriptions
# print(content['articles'])
for index, article in enumerate(content['articles']):
  if index < 5:
    # print(article['title']  + '\n')
    # print(article['description'] + '\n')
    print(f"{article['title']}  <---->  {article['description']}")