"""Platzi Views"""
from django.http import HttpResponse
from datetime import datetime

from django.http.response import JsonResponse

def hello_world(request):
  """Return a greeting message."""
  now = datetime.now().strftime("%Y-%m-%d")
  return HttpResponse('Oh, hi! Current time is {now}'.format(
    now = str(now)))
  
def hi(request):
  
  numbers_str = request.GET.get('numbers')
  #print(type(numbers_str))
  sorted_numbers = sorted(map(int, numbers_str.split(',')))
  print(sorted_numbers)
  data = {
    'status': 'ok',
    'data': sorted_numbers
  }
  return JsonResponse(data, safe=False)