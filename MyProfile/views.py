from django.shortcuts import render

def index(request):
    try:
        return render(request, 'index.html')

    except Exception as error:
        return render(request, 'index.html', {'Error':error})                