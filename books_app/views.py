from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'home.html')

def category(request):
    return render (request,'Category.html')


def book(request):
    return render (request,'book.html')

def user_page(request):
    return render (request,'user_page.html')



def home(request):
    return render (request,'About_us.html')

