from django.shortcuts import render, redirect
from .models import QRCode

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        name = request.POST['link']
        QRCode.objects.create(name=name, title=title)
        return redirect('/')
    a = QRCode.objects.order_by('-id').all()


    return render(request, 'index.html', {'a':a})


def delete(request, id):
    qr = QRCode.objects.get(id=id)
    qr.delete()
    return redirect('/')