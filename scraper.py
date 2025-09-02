import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_verge_ai():
    """Stiahne AI články z The Verge"""
    url = "https://www.theverge.com/ai-artificial-intelligence"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        
        # Hľadáme články na stránke
        for article in soup.find_all('article', limit=5):  # Prvých 5 článkov
            title_element = article.find('h2')
            if title_element:
                title = title_element.get_text().strip()
                link_element = title_element.find('a')
                
                if link_element:
                    link = "https://www.theverge.com" + link_element.get('href')
                    
                    articles.append({
                        'title': title,
                        'url': link,
                        'source': 'The Verge',
                        'scraped_at': datetime.now().isoformat()
                    })
        
        return articles
    
    except Exception as e:
        print(f"Chyba pri scrapingu: {e}")
        return []

if __name__ == "__main__":
    print("🤖 Spúšťam AI News Scraper...")
    articles = scrape_verge_ai()
    
    print(f"\n📰 Našiel som {len(articles)} článkov:\n")
    
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")
        print(f"   🔗 {article['url']}")
        print()
