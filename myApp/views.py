from django.shortcuts import render, redirect
from .models import URL
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        url = URL(original_url=original_url)
        url.save()
        return render(request, 'home.html', {'short_url': url.short_url})
    return render(request, 'home.html')

def redirect_to_url(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return HttpResponse('Short URL not found', status=404)
