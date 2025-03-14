from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to SClass Home Page</h1>")
