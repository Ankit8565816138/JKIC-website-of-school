from django.shortcuts import render,redirect

# Create your views here.
def index (request):
    return render(request,'index.html')
def about (request):
    return render(request,'about.html')
def notice_news(request):
    return render(request,'notice_news.html')
def contact_us(request):
    return render(request,'contact_us.html')
def help(request):
    return render(request,'help.html')