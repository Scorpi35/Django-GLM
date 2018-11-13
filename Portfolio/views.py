from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Portfolio



# Create your views here.

def index(request):
    template = loader.get_template('Portfolio/index.html')
    context = {

    }
    
    return HttpResponse(template.render(context, request))


# For posting portfolio
def post(request):

    if request.method == 'POST':
        post = Portfolio()
        post.Category = request.POST.get('Portfolio_Category')
        post.Title = request.POST.get('Portfolio_Title')
        post.Location = request.POST.get('Portfolio_Location')
        post.P_Language = request.POST.get('Portfolio_Language')
        post.Github = request.POST.get('Portfolio_Github')
        post.Level = request.POST.get('Portfolio_Level')
        post.save()

        return redirect("http://127.0.0.1:8000/Portfolio/")

    else:
        template = loader.get_template('Portfolio/Post.html')
        context = {

        }

        return HttpResponse(template.render(context, request))


# Function to show Portfolio of selected Category
def Portfolio_Show(request):
    template = loader.get_template('Portfolio/index.html')
    title = []
    location = []
    language = []
    github = []
    level = []
    if request.method == 'GET':
        category = request.GET['Portfolio_Category']
        for p in Portfolio.objects.raw(
                'SELECT id, Title, Location, P_Language, Github, Level '
                'FROM Portfolio_portfolio '
                'WHERE Category=%s', [category]
        ):
            title.append(p.Title)
            location.append(p.Location)
            language.append(p.P_Language)
            github.append(p.Github)
            level.append(p.Level)

    return JsonResponse({
        'Title': title,
        'Location': location,
        'Language': language,
        'Github': github,
        'Level': level,
        'Total': len(title),
    })
