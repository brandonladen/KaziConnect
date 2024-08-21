from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Successfully Logged in")

def login(request):
    if request.method == 'POST':
        email = ""
        password = ""