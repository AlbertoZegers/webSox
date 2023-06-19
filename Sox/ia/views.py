from django.shortcuts import render
#import subprocess

# Create your views here.
def feedback(request):
    return render(request, 'ia/pagFeedback.html')
def visualizacion(request):
    #comando = 'python manage.py shell -c "exec(open(\'Sox.py\').read())"'
    #subprocess.Popen(comando, shell=True)
    return render(request, 'ia/pagVisualizacion.html')