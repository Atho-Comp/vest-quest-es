from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method != 'POST':
        return render(request, 'home/index.html')

    name = request.POST.get('name')
    last_name = request.POST.get('lastname')
    email = request.POST.get('email')

    return render(request, 'home/index.html')