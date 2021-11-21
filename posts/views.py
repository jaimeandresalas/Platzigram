from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
posts = [
  {
    'name': 'Mont Blac',
    'user': 'Yesica Cortes',
    'timestamp': datetime.now().strftime('%Y-%m-%d'),
    'picture': 'https://evalart.com/wp-content/uploads/2019/03/PruebasProgramacion.png'
  }
]


def list_posts(request):
  """List all posts"""
  content = []
  for post in posts:
    content.append("""
                   <p><strong>{name}</strong></p>
                   <p><strong>{user}</strong></p>
                   <p><strong>{timestamp}</strong></p>
                   <figure><img src="{picture}/"></figure>
                   """.format(**post))
  return HttpResponse('<br>'.join(content))