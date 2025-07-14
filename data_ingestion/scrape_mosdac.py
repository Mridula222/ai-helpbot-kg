import requests
from bs4 import BeautifulSoup

def scrape_mosdac_faq(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    faqs = []
    # Adjust selectors based on MOSDAC HTML structure
    questions = soup.find_all("h3")
    answers = soup.find_all("p")

    for q, a in zip(questions, answers):
        faqs.append({
            "question": q.get_text(strip=True),
            "answer": a.get_text(strip=True)
        })
    
    return faqs

if __name__ == "__main__":
    url = "https://mosdac.gov.in/faqs"  # example FAQ URL
    faqs = scrape_mosdac_faq(url)
    for f in faqs:
        print(f)
