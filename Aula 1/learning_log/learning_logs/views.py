from django.shortcuts import render

# Create your views here.
def index(request):
    """Irá exibir a pagina inicial do site Learning Logs"""
    return render(request, 'learning_logs/index.html')