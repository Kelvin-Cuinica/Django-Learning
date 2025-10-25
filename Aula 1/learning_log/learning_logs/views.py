from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Irá exibir a pagina inicial do site Learning Logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Ira exibir a pagina dos Topicos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)
