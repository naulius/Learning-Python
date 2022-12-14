# Rules of web scraping:
      # Always try to get permission before scraping
      # If you make too many requests or attempts your IP could be blocked.
      # Some sides automatically block scraping software.

# Limitations of web scraping:
      # Every web scraping script is unique.
      # A slight change or update to a website may break your web scraping script.

import requests
import bs4

result = requests.get("http://www.example.com")
type(result)
print(requests.models.Response)
print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
print(soup.select("title"))
print(soup.select("p"))

