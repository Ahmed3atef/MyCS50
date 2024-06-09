from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Projects


class PortfolioView(ListView):
    model=Projects
    template_name = "portfolio/index.html"
    

class PortfolioAddView(CreateView):
    model = Projects
    template_name = 'portfolio/add_project.html'
    fields = ['img_url','url', 'name']