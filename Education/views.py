from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Creating view for Education page
def index(request):
    template = loader.get_template('Education/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


