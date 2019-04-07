import json
import boto3

def lambda_handler(event, context):
	request = event['request']

	if request['type'] == 'IntentRequest':
		intent = request['intent']
		if intent['name'] == 'MoveBotForward':
			move_bot_forward(intent)
			return build_response('Moving bot to target position')

		# Default intents provided by Amazon
		# We need to implement them
		elif intent['name'] == 'AMAZON.FallbackIntent':
			return build_reponse('I didn\'t understand that')
		elif intent['name'] == 'AMAZON.HelpIntent':
			return build_response('Ask me to move bot forward')
		elif intent['name'] == 'AMAZON.CancelIntent' or intent['name'] == 'AMAZON.StopIntent':
			return build_response('Goodbye')
			
def build_response(text):
	return {
		'version': '1.0',
		'response': {
			'outputSpeech': {
				'type': 'PlainText',
				'text': text
			},
			'shouldEndSession': True
		}
		}

def move_bot_forward(intent):
	request = 'move_bot_forward'
	boto3.client('sqs').send_message(QueueUrl='https://sqs.eu-west-1.amazonaws.com/229803897151/ev3', MessageBody=request)
