from fastapi import FastAPI
from scraper import scrape_verge_ai

app = FastAPI(title="AI News Scraper", version="1.0.0")

@app.get("/")
def home():
    return {"message": "AI News Scraper je spustený! Choď na /articles"}

@app.get("/articles")
def get_articles():
    articles = scrape_verge_ai()
    return {
        "count": len(articles),
        "articles": articles
    }
