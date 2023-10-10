import requests
import json, os
from dotenv import load_dotenv

class MongoDBDataAPI:
    """
    A class to interact with MongoDB Data API for specific operations.
    
    Attributes:
        url (str): The MongoDB Data API endpoint URL.
        MONGODB_API_KEY (str): The API key for MongoDB Data API.
        collection_name (str): The name of the MongoDB collection.
        database_name (str): The name of the MongoDB database.
        headers (dict): The headers for the API requests.
    """
    
    def __init__(self, collection_name, database_name):
        """
        Initializes the MongoDBDataAPI with the given collection and database names.
        
        Args:
            collection_name (str): The name of the MongoDB collection.
            database_name (str): The name of the MongoDB database.
        """
        load_dotenv()
        self.url = "https://us-east-2.aws.data.mongodb-api.com/app/data-wjpob/endpoint/data/v1/action/findOne"
        self.MONGODB_API_KEY = os.getenv("MONGODB_API_KEY")
        self.collection_name = collection_name
        self.database_name = database_name
        self.headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': self.MONGODB_API_KEY,
        }

    def _fetch_data(self, filter_condition):
        """
        Fetches data from MongoDB based on the given filter condition.
        
        Args:
            filter_condition (dict): The condition to filter the data.
            
        Returns:
            list: A list of filtered data from MongoDB.
        """
        # Update the URL to use the 'find' action instead of 'findOne'
        find_url = self.url.replace("findOne", "find")
        
        payload = json.dumps({
            "collection": self.collection_name,
            "database": self.database_name,
            "dataSource": "social-media-bots",
            "filter": filter_condition,
        })
        response = requests.post(find_url, headers=self.headers, data=payload)
        return response.json()

    def get_ai_generated_messages_post_leads(self):
        """
        Fetches messages that don't have the `comment_author` key.
        
        Returns:
            list: A list of messages without the `comment_author` key.
        """
        filter_condition = {
            "comment_author": {"$exists": False}
        }
        return self._fetch_data(filter_condition)

    def get_ai_generated_messages_commenter_leads(self):
        """
        Fetches messages that have the `comment_author` key.
        
        Returns:
            list: A list of messages with the `comment_author` key.
        """
        filter_condition = {
            "comment_author": {"$exists": True}
        }
        return self._fetch_data(filter_condition)

    def remove_message(self, message_id: str):
	    """
	    Removes a message based on the provided `_id`.
	    
	    Args:
	        message_id (str): The ObjectId of the document to be removed.
	        
	    Returns:
	        dict: The response from the MongoDB Data API after the delete operation.
	    """
	    # Ensure you're using the correct endpoint for deletion
	    remove_url = self.url.replace("findOne", "deleteOne")
	    
	    # Filter condition to match documents with the specified _id
	    filter_condition = {
	        "_id": {"$oid": message_id}  # Use the $oid operator to specify an ObjectId
	    }
	    
	    payload = json.dumps({
	        "collection": self.collection_name,
	        "database": self.database_name,
	        "dataSource": "social-media-bots",
	        "filter": filter_condition
	    })
	    response = requests.post(remove_url, headers=self.headers, data=payload)
	    print(message_id)
	    print(response.json())
	    return response.json()
    
# Usage:
db = MongoDBDataAPI("AI Generated Messages", "Reddit_Engagement_Bot")
#post_leads = db.get_ai_generated_messages_post_leads()
# commenter_leads = db.get_ai_generated_messages_commenter_leads()
#print("POST LEADS:\n", post_leads)
# print("COMMENTER LEADS:\n", commenter_leads)
# db.remove_message("<cold_dm_starter_value>", "<title_value>")
