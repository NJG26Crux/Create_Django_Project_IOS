## new_app ##
from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    context = {}
    return render(request, "new_app/index.html", context)

