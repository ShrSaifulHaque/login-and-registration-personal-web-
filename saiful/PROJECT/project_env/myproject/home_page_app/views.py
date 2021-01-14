from django.shortcuts import render

def homePage(request):
    return render(request, 'home_page_app/home_page.html')