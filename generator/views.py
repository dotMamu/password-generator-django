import random
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def about(request):
    """
    It takes a request, and returns a response
    
    :param request: The request is an HttpRequest object. It contains metadata about the request. We'll
    see more of this later
    :return: the render function.
    """
    return render(request, 'generator/about.html')

def home(request):
    """
    It takes a request and returns a response.
    
    :param request: The request is a parameter that is always passed to a view function, and it contains
    all of the information sent by the user’s browser
    :return: The home.html file is being returned.
    """
    return render(request, 'generator/home.html')

def password(request):
    """
    It takes the length of the password, and the checkboxes, and generates a password with the length
    and the characters that the user has selected
    
    :param request: This is the request object that is sent to the view
    :return: the render function.
    """

    characters = list('abcdeabcdefghijklmnopqrstuvwxyz')
    generatedPassword=''

    
    length = int(request.GET.get('length'))

    if(request.GET.get('uppercase')):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if(request.GET.get('special')):
        characters.extend(list("-+_!$%&/()=?¡@~`^_:;[]*¿"))

    
    if(request.GET.get('numbers')):
        characters.extend(list("0123456789"))

    for i in range(length):
        generatedPassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':generatedPassword})