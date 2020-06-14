from django.http import HttpResponse

def hello_main(request):
    helloString = "Hello World !"
    return HttpResponse(helloString)

def about(request):
    aboutString = "This is an about section..."
    return HttpResponse(aboutString)