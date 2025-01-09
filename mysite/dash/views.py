from django.shortcuts import render
from django.views.generic import TemplateView

#from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the dash index.")


def index(request):
    return render(request, 'dash/index.html')

def dash_view(request):
    return render(request, 'dash/index.html')

class DashIndexView(TemplateView):
    template_name = 'dash/index.html'

    """
        Go the polls app TODO:
    """
    def go_to_polls(self):
        return None
