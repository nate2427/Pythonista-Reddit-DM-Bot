import praw, os, requests
from dotenv import load_dotenv

load_dotenv()

# Initialize the Reddit instance
reddit = praw.Reddit(
	client_id=os.getenv('REDDIT_CLIENT_ID'),
	client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
	user_agent='your_user_agent',
	username=os.getenv('REDDIT_USERNAME'),
	password=os.getenv('REDDIT_PASSWORD')
)

# Send a private messagem

def send_message(username, message):
    """
    Send a private message to a Reddit user with the first few words of the message as the subject.

    Args:
    - username (str): The Reddit username of the recipient.
    - message (str): The content of the message.
    """
    # Use the first few words (or the entire message if it's short) as the subject
    subject = ' '.join(message.split()[:5])  # Adjust the number 5 as needed
    reddit.redditor(username).message(subject=subject, message=message)


# send_message("gpt-instructor", "Yoooooo, whats the word, my brother?")
