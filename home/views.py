from django.shortcuts import render, HttpResponse

# Create your views here.
def chat(request):
    return render(request, 'index.html')

def chatAPI(request):
    return HttpResponse("Chat API working")