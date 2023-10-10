import ui
from mongodb_custom_sdk import db
from reddit_bot import send_message

messages = [
 
]

current_index = 0
isDarkModeEnabled = False

def load_post_leads_view(sender):
	global messages
	global isDarkModeEnabled
	global current_index
	current_index = 0
	# load post leads from db
	messages = db.get_ai_generated_messages_post_leads()["documents"]
	v = ui.load_view("Post Leads")
	v.name = 'Post Leads'
	test_table_data = ui.ListDataSource([])

	originalPostView = v["originalPostView"]
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	# reddit post details setup
	originalPostView["postTitle"].text = messages[current_index]["title"]
	originalPostView["postDetails"].text = messages[current_index]["body"]
	originalPostView["postAuthor"].text = messages[current_index]["author"]
	originalPostView["postSubreddit"].text = messages[current_index]["subreddit"]
	
	# ai generated message setup
	aiGeneratedMessageView["aiMessage"].text = messages[current_index]["cold_dm_starter"]
	
	# set page color theme
	if isDarkModeEnabled:
		v.background_color = "#121212"
		originalPostView["postTitle"].text_color = "#ffffff"
		originalPostView["postDetails"].text_color = "#ffffff"
		originalPostView["postAuthor"].text_color = "#ffffff"
		originalPostView["postSubreddit"].text_color = "#ffffff"
		originalPostView["originalPostLabel"].text_color = "#ffffff"
		originalPostView["postTitleLabel"].text_color = "#ffffff"
		originalPostView["postAuthorLabel"].text_color = "#ffffff"
		originalPostView["postSubredditLabel"].text_color = "#ffffff"
		originalPostView["postDetailsLabel"].text_color = "#ffffff"
		aiGeneratedMessageView["aiMessage"].text_color = "#ffffff"
		aiGeneratedMessageView["aiGeneratedMessageLabel"].text_color = "#ffffff"
		aiGeneratedMessageView["messageLabel"].text_color = "#ffffff"
		
	else:
		v.background_color = "#ffffff"
	
	sender.navigation_view.push_view(v)


def load_commenter_leads_view(sender):
	v = ui.load_view("Commenter Leads")
	v.name = 'Commenter Leads'
	global messages
	global current_index
	global isDarkModeEnabled
	current_index = 0
	# load post leads from db
	messages = db.get_ai_generated_messages_commenter_leads()["documents"]
	
	print(messages[0].keys())
	
	# grab the views
	originalPostView = v["originalPostView"]
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	commenterInfoView = v["commenterInfoView"]
	
	# set page color theme
	if isDarkModeEnabled:
		v.background_color = "#121212"
		originalPostView["postTitle"].text_color = "#ffffff"
		originalPostView["postDetails"].text_color = "#ffffff"
		originalPostView["postAuthor"].text_color = "#ffffff"
		originalPostView["postSubreddit"].text_color = "#ffffff"
		originalPostView["originalPostLabel"].text_color = "#ffffff"
		originalPostView["postTitleLabel"].text_color = "#ffffff"
		originalPostView["postAuthorLabel"].text_color = "#ffffff"
		originalPostView["postSubredditLabel"].text_color = "#ffffff"
		originalPostView["postDetailsLabel"].text_color = "#ffffff"
		commenterInfoView["commenterAuthor"].text_color = "#ffffff"
		commenterInfoView["commentTextView"].text_color = "#ffffff"
		
		commenterInfoView["commenterInfoLabel"].text_color = "#ffffff"
		commenterInfoView["commenterAuthorLabel"].text_color = "#ffffff"
		commenterInfoView["commentLabel"].text_color = "#ffffff"
		
		aiGeneratedMessageView["aiMessage"].text_color = "#ffffff"
		aiGeneratedMessageView["aiGeneratedMessageLabel"].text_color = "#ffffff"
		aiGeneratedMessageView["messageLabel"].text_color = "#ffffff"
	
	#  details setup
	originalPostView["postTitle"].text = messages[current_index]["post_title"]
	originalPostView["postDetails"].text = messages[current_index]["post_body"]
	originalPostView["postAuthor"].text = messages[current_index]["post_author"]
	originalPostView["postSubreddit"].text = messages[current_index]["subreddit"]
	
	# commenter info
	commenterInfoView["commenterAuthor"].text = messages[current_index]["comment_author"]
	commenterInfoView["commentTextView"].text = messages[current_index]["comment_body"]
	
	# ai generated message setup
	aiGeneratedMessageView["aiMessage"].text = messages[current_index]["cold_dm_starter"]
	sender.navigation_view.push_view(v)

def go_foward_to_next_post_lead(sender):
	global current_index 
	global messages
	current_index = (1 + current_index) % len(messages)
	v = sender.superview.superview
	
	# grab the views
	originalPostView = v["originalPostView"]
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	
	
	# reddit post details setup
	originalPostView["postTitle"].text = messages[current_index]["title"]
	originalPostView["postDetails"].text = messages[current_index]["body"]
	originalPostView["postAuthor"].text = messages[current_index]["author"]
	originalPostView["postSubreddit"].text = messages[current_index]["subreddit"]
	
	# ai generated message setup
	aiGeneratedMessageView["aiMessage"].text = messages[current_index]["cold_dm_starter"]
	
	v.set_needs_display()
	
	
def go_backward_to_prev_post_lead(sender):
	global current_index 
	global messages
	current_index = 0 if current_index == 0 else (current_index - 1) % len(messages)
	v = sender.superview.superview
	
	# grab the views
	originalPostView = v["originalPostView"]
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	
	
	# reddit post details setup
	originalPostView["postTitle"].text = messages[current_index]["title"]
	originalPostView["postDetails"].text = messages[current_index]["body"]
	originalPostView["postAuthor"].text = messages[current_index]["author"]
	originalPostView["postSubreddit"].text = messages[current_index]["subreddit"]
	
	# ai generated message setup
	aiGeneratedMessageView["aiMessage"].text = messages[current_index]["cold_dm_starter"]
	
	v.set_needs_display()
	
def go_foward_to_next_commenter_lead(sender):
	global current_index 
	global messages
	current_index = (1 + current_index) % len(messages)
	v = sender.superview.superview
	
	# grab the views
	originalPostView = v["originalPostView"]
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	commenterInfoView = v["commenterInfoView"]
	
	#  details setup
	originalPostView["postTitle"].text = messages[current_index]["post_title"]
	originalPostView["postDetails"].text = messages[current_index]["post_body"]
	originalPostView["postAuthor"].text = messages[current_index]["post_author"]
	originalPostView["postSubreddit"].text = messages[current_index]["subreddit"]
	
	# commenter info
	commenterInfoView["commenterAuthor"].text = messages[current_index]["comment_author"]
	commenterInfoView["commentTextView"].text = messages[current_index]["comment_body"]
	
	# ai generated message setup
	aiGeneratedMessageView["aiMessage"].text = messages[current_index]["cold_dm_starter"]
	
	v.set_needs_display()
	

def go_backward_to_prev_commenter_lead(sender):
	global current_index 
	global messages
	current_index = 0 if current_index == 0 else (current_index - 1) % len(messages)
	v = sender.superview.superview
	
	# grab the views
	originalPostView = v["originalPostView"]
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	commenterInfoView = v["commenterInfoView"]
	
	#  details setup
	originalPostView["postTitle"].text = messages[current_index]["post_title"]
	originalPostView["postDetails"].text = messages[current_index]["post_body"]
	originalPostView["postAuthor"].text = messages[current_index]["post_author"]
	originalPostView["postSubreddit"].text = messages[current_index]["subreddit"]
	
	# commenter info
	commenterInfoView["commenterAuthor"].text = messages[current_index]["comment_author"]
	commenterInfoView["commentTextView"].text = messages[current_index]["comment_body"]
	
	# ai generated message setup
	aiGeneratedMessageView["aiMessage"].text = messages[current_index]["cold_dm_starter"]
	
	v.set_needs_display()


def send_message_and_switch_message_post_leads(sender):
	# grab the message and the post author username to send it to
	global current_index
	v = sender.superview.superview
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	originalPostView = v["originalPostView"]
	ai_message = aiGeneratedMessageView["aiMessage"].text
	post_author_username = originalPostView["postAuthor"].text
	post_title = originalPostView["postTitle"].text
	# send the message
	send_message(post_author_username, ai_message)
	# remove message from db
	db.remove_message(messages[current_index]["_id"])
	# remove message from app state
	messages.pop(current_index)
	# move to the next step
	current_index -= 1
	go_foward_to_next_post_lead(sender)

		
def send_message_and_switch_message_commenter_leads(sender):
	# grab the message and the post author username to send it to
	global current_index
	v = sender.superview.superview
	aiGeneratedMessageView = v["aiGeneratedMessageView"]
	commenterInfoView = v["commenterInfoView"]
	ai_message = aiGeneratedMessageView["aiMessage"].text
	commenter_username = commenterInfoView["commenterAuthor"].text
	# send the message
	send_message(commenter_username, ai_message)
	# remove message from db
	db.remove_message(messages[current_index]["_id"])
	# remove message from app state
	messages.pop(current_index)
	# move to the next step
	current_index -= 1
	go_foward_to_next_commenter_lead(sender)
	
	
def regenerate_ai_msg_post_lead(sender):
	pass
	
	
def toggle_dark_theme(sender):
	global isDarkModeEnabled
	v = sender.superview.superview
	if not isDarkModeEnabled:
		v.background_color = '#121212'
	else:
		v.background_color = '#ffffff'
	v.set_needs_display()
	isDarkModeEnabled =  (not isDarkModeEnabled)
	

root_view = ui.load_view("Dashboard")
root_view.name = 'Dashboard'

nav_view = ui.NavigationView(root_view)
nav_view.present('fullscreen', hide_title_bar=True)

