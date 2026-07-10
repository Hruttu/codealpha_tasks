import requests
from bs4 import BeautifulSoup
import pandas as pd

# Empty list to store all scraped data
all_quotes = []

# Loop through 5 pages
for page in range(1, 6):
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text   = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags   = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

        all_quotes.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })

    print(f"Page {page} scraped ✓")

# Save to CSV
df = pd.DataFrame(all_quotes)
df.to_csv("quotes_dataset.csv", index=False)

print(f"\nDone! {len(all_quotes)} quotes saved to quotes_dataset.csv")