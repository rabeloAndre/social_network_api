# Python program to read 
# json file 

from social.models import *

import json
f = open('db.json','r')
data = json.load(f)

for i in data['users']:
	name = i['name']
	username = i['username']
	email = i['email']
	phone = i['phone']
	website = i['website']
	profile = Profile.objects.create(name=name,username=username,email=email,phone=phone,website=website)

for i in data['posts']:
	title = i['title']
	body = i['body']
	userId = Profile.objects.get(id=i['userId'])
	post = Post.objects.create(title=title,body=body,userId=userId)

for i in data['comments']:
	name = i['name']
	email = i['email']
	body = i['body']
	postId = Post.objects.get(id=i['postId'])
	comment = Comment.objects.create(name=name,email=email,body=body,postId=postId)

f.close()