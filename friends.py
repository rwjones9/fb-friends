import json

with open('friends_added.json', 'r') as f:
	friends_dict = json.load(f)

fh = open('friends.txt', 'w')
for item in friends_dict['friends']:
	print(item['name'])
	fh.write(item['name'])
	fh.write('\n')
fh.close()
