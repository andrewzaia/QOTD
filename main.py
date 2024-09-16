import requests

def quote_of_the_day():
    url = "https://api.quotable.io/random" # Need to update URL to a new random one

    response = requests.get(url)

    if response.ok:
        data = response.json()
        quote = data['content']
        author = data['author']
        return f"{quote}\n- {author}"
    else:
        return f"Error accessing API. Response: {response.status_code}"

get_quote = quote_of_the_day()
print(get_quote)
input("Press enter to close window.")
