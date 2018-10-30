from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Creating views of the HomePage app

def index(request):
    template = loader.get_template('HomePage/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
