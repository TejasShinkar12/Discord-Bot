import random
from get_mail import new_mail
from reddit_posts import get_posts


# This function takes a message as input and returns a string response.
# It handles various commands in the message and generates corresponding responses.
def handle_response(message) -> str:
  # Convert the message to lowercase for case-insensitive comparisons.
  p_message = message.lower()

  # Check if the message is 'news'.
  if p_message == 'news':
    # Fetch new mail data using the 'new_mail' function.
    news = new_mail()

    # Yield each item from the 'news' list, excluding the first 6 and last 6 elements.
    for i in news[6:-6]:
      yield i  # Yielding individual items from the 'news' list.

  # Check if the message is 'reddit'.
  if message == 'reddit':
    # Fetch top Reddit posts using the 'get_posts' function.
    top_posts = get_posts()

    # Yield the 'top_posts' as a generator.
    yield top_posts  # Yielding the 'top_posts' generator.

  # Check if the message is 'hello'.
  if p_message == 'hello':
    return 'Hey there!'  # Return a friendly greeting.

  # Check if the message is 'roll'.
  if p_message == 'roll':
    # Generate a random integer between 1 and 6 and convert it to a string.
    return str(random.randint(1, 6))

  # Check if the message is '!help'.
  if p_message == '!help':
    # Return a help message in markdown format.
    return "`This is a help message that you can modify.`"  # Help message in markdown format.
