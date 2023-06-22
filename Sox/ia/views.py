from django.shortcuts import render
from .forms import ComentarioForm
#import subprocess

# Create your views here.
def feedback(request):
    data = {'form' : ComentarioForm} 
    return render(request, 'ia/pagFeedback.html')

def visualizacion(request):
    #comando = 'python manage.py shell -c "exec(open(\'Sox.py\').read())"'
    #subprocess.Popen(comando, shell=True)
    return render(request, 'ia/pagVisualizacion.html')