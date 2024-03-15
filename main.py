import requests
import bs4


def quote_of_the_day():
    url = "https://www.brainyquote.com/quote_of_the_day"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=header)

    if response.ok:
        site = bs4.BeautifulSoup(response.text, "html.parser")
        quote_container = site.find("img", {"class": "p-qotd"})
        if quote_container and quote_container.has_attr("alt"):
            # Split quote
            split_quote = quote_container["alt"].split(" - ")
            return f"{split_quote[0]}\n- {split_quote[1]}"
        else:
            return "Quote not found."
    else:
        return f"Error accessing website. Response: {response}"


get_quote = quote_of_the_day()
print(get_quote)
input("Press enter to close window.")