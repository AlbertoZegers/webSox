from django.shortcuts import render

# Create your views here.
def feedback(request):
    return render(request, 'ia/pagFeedback.html')
def visualizacion(request):
    return render(request, 'ia/pagVisualizacion.html')