import requests
from bs4 import BeautifulSoup

def fetch_tulja_bhavani_info():
    url = "https://en.wikipedia.org/wiki/Tulja_Bhavani_Temple"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the first paragraph of the article
    first_paragraph = soup.find('div', {'class': 'reflist'})
    if first_paragraph:
        print(first_paragraph.text.strip())
    else:
        print("Information not found.")

if __name__ == "__main__":
    fetch_tulja_bhavani_info()
