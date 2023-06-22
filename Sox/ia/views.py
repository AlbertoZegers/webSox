from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComentarioForm
from .models import Comentario
#import subprocess

# Create your views here.
def feedback(request):
    comentarios=Comentario.objects.all()
    data = {'form' : ComentarioForm(initial={'usuario': request.user}), 'comentarios': comentarios}
    if request.method == 'POST':
         formulario=ComentarioForm(data=request.POST)
         if formulario.is_valid():
             formulario.save()
         else:
            formulario = ComentarioForm()
    return render(request, 'ia/pagFeedback.html', data)

def visualizacion(request):
    #comando = 'python manage.py shell -c "exec(open(\'Sox.py\').read())"'
    #subprocess.Popen(comando, shell=True)
    return render(request, 'ia/pagVisualizacion.html')

def modificar(request, id):
    comentario=get_object_or_404(Comentario, id=id)
    data = {'form': ComentarioForm(instance=comentario, initial={'usuario': request.user})}
    if request.method=='POST':
        formulario= ComentarioForm(data=request.POST, instance=comentario)
        if formulario.is_valid():
            formulario.save()
            return redirect('feedback')
        else:
           formulario=ComentarioForm() 
    return render(request, 'ia/modificar.html', data)

def eliminar(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    comentario.delete()
    return redirect('feedback')