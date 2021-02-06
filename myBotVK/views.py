from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import vk
import random

session = vk.Session(access_token='eee89cf609325d2d96e69ff0569c61a5b155c11a6adb72c45f5e2753ec43057e46fac96549f97d7a59e03')
vk_api=vk.API(session)

@csrf_exempt
def init(request):
	body = json.loads(request.body)
	if body == { "type": "confirmation", "group_id": 202246294 }:
		return HttpResponse("b99cbc0b")

@csrf_exempt
def index(request):
	body = json.loads(request.body)
	print(body)
	if body["type"] == 'message_new':
		user_id = body["object"]["user_id"]
		if body["object"]["body"] != "0":
			messages = body["object"]["body"]
			vk_api.messages.send(user_id=user_id, message=messages, random_id=random.randint(1,50000000000000000000000) ,v=5.103)
	return HttpResponse("ok")