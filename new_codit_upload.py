import praw, login_info, json
reddit = login_info.reddit

url = "https://www.reddit.com/r/teenagersbutpog/comments/pjg3lj/coddit_20_but_on_a_reddit_post_cause_im_stupid/"
post = reddit.submission(url = url)
data = {}

list_of_users = []

def get_by_posts(contribution_data):
	return contribution_data[1]

def get_by_comments(contribution_data):
	return contribution_data[2]

def get_by_contributions(contribution_data):
	return contribution_data[1] + contribution_data[2]


with open("data.json") as data_file:
	data = json.load(data_file)

	for user in data:
		list_of_users.append([user, data.get(user)[0], data.get(user)[1]])

	list_of_users.sort(key = get_by_comments, reverse = True)

edit_string = "User: ----------------------------- Posts: ----- Comments: \r\r"
other_space_length = " -------- "
for i in list_of_users:
	space_length = "  "
	for j in range(34 - len(str(i[0]))):
		space_length += "-"
	space_length += "  "
	edit_string += ""
	edit_string += str(i[0])
	edit_string += str(space_length) + str(i[1])
	edit_string += str(other_space_length) + str(i[2]) + "\r\r"
post.edit(edit_string)