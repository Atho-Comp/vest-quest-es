from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    if request.method != 'POST':
        return render(request, 'home/index.html')

    name = request.POST.get('name')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')

    user = User(
        name=name,
        last_name=last_name,
        email=email,
    )

    if User.objects.filter(email=email).exists():
        return render(request, 'home/index.html', {
            'enviado': False,
        })

    user.save()

    return render(request, 'home/index.html', {
        'enviado': True,
    })