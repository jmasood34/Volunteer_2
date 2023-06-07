import requests


def daily_quote():
    """
    This function gets a random quote from the Quotable API.

    Returns:
        A tuple of (quote, author) if the request was successful, or None if the request failed.
    """

    # Make a request to the Quotable API.
    response = requests.get("https://api.quotable.io/random")

    # Check if the request was successful.
    if response.status_code == 200:
        # Get the quote and author from the response data.
        data = response.json()
        quote = data['content']
        author = data['author']

        # Return the quote and author.
        return quote, author

    # If the request was not successful, return None.
    else:
        return None
