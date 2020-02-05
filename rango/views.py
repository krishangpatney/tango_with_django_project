from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessages'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html') 