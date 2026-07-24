import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")

            print("\n===== TOP HEADLINES =====\n")

            # Extract headlines
            headlines = soup.find_all(["h1", "h2", "h3"])

            count = 1

            for headline in headlines:
                title = headline.get_text(strip=True)

                if title:
                    print(f"{count}. {title}")
                    count += 1

                if count > 10:
                    break

        else:
            print("Unable to access website.")

    except requests.exceptions.RequestException:
        print("Error: Unable to connect to website.")

    except Exception as e:
        print("Error occurred:", e)


def main():

    print("===== BASIC WEB SCRAPER =====")

    # Example news website
    url = "https://www.bbc.com/news"

    scrape_headlines(url)


if __name__ == "__main__":
    main()