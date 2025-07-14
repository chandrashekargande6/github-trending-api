import requests
from bs4 import BeautifulSoup

def fetch_trending_repos(limit=10):
    url = "https://github.com/trending"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    repo_list = []

    # Select all trending repo cards
    repo_items = soup.find_all("article", class_="Box-row")[:limit]

    for repo in repo_items:
        try:
            # Get the repo name from the href
            a_tag = repo.select_one("h2.h3 a")
            if a_tag and a_tag.has_attr("href"):
                name = a_tag["href"].strip("/")  # e.g., /vercel/next.js → vercel/next.js
            else:
                name = "Unknown"

            # Description (optional)
            description_tag = repo.find("p")
            description = description_tag.get_text(strip=True) if description_tag else "No description"

            # Stars
            stars_tag = repo.find("a", href=lambda x: x and x.endswith("/stargazers"))
            stars = stars_tag.get_text(strip=True) if stars_tag else "N/A"

            # Add to list
            repo_list.append({
                "name": name,
                "description": description,
                "stars": stars
            })

        except Exception as e:
            print(f"⚠️ Skipping repo due to error: {e}")
            continue

    return repo_list
