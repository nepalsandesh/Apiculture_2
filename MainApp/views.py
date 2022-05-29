from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index1.html')


def blog(request):
    return render(request, 'blog1.html')

def blog_single(request):
    return render(request, 'blog-single1.html')