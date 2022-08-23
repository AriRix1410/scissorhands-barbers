from django.shortcuts import render

# Create your views here.


def home(request):
    '''
    Renders the home page.
    '''
    return render(request, 'index.html')
