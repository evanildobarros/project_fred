from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


chatbot = ChatBot("Ron Obvious")


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body)
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)




def main(request, template_name="index.html"):
	context = {'title': 'Fred Chatbot Version 1.0'}
	return render_to_response(template_name, context)