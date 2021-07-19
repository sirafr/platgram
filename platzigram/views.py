"""PLATZIGRAM VIEWS"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs.')
	return HttpResponse(f"HOLA MUNDO! server time: {now}")


def hi(request):
	"""hi"""
	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	# import pdb; pdb.set_trace()

	# Tranformacion a API
	data = {
		'status':'ok',
		'numbers':sorted_ints,
		'message':'Integers sorted sucessfully!'
	}

	# Regresamos la data en formato JSON
	return HttpResponse(json.dumps(data,indent=3,content_type='application/json')




