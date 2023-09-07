import requests
from bs4 import BeautifulSoup

url = 'https://www.nationalgeographic.com/science/'

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')

    article_titles = []
    article_summaries = []

    article_elements = soup.find_all('article', class_='Card_gridCol-uwv0jr-0 Card_gridCol__Wide-uwv0jr-1 fNEVAd')
    for article_element in article_elements:
        title = article_element.find('h2', class_='Heading-sc-1v5asz5-0 fFOaSa Text-sc-1v5asz5-1 ekPvXw').text.strip()
        summary = article_element.find('p', class_='Text-sc-1v5asz5-1 drqfqK').text.strip()
        article_titles.append(title)
        article_summaries.append(summary)

    for i in range(len(article_titles)):
        print(f"Title: {article_titles[i]}")
        print(f"Summary: {article_summaries[i]}")
        print()

    with open('science_articles.txt', 'w', encoding='utf-8') as file:
        for i in range(len(article_titles)):
            file.write(f"Title: {article_titles[i]}\n")
            file.write(f"Summary: {article_summaries[i]}\n")
            file.write('\n')

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
