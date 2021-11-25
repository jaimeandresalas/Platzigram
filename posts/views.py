from django.shortcuts import render
from datetime import datetime
# Create your views here.
posts = [
    {
        'title': 'Mont Blac',
        'user': {'name': 'Yesica Cortes',
                 'picture': 'https://evalart.com/wp-content/uploads/2019/03/PruebasProgramacion.png'
                 },
        'timestamp': datetime.now().strftime('%Y-%m-%d'),

    }
]


def list_posts(request):
    """List all posts"""
    return render(request, 'feed.html', {'posts': posts})
