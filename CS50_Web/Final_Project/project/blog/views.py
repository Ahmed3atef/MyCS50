from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class Index(ListView):
    model=Post
    template_name="blog/index.html"
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
    model=Post
    template_name='blog/post_new.html'
    form_class = PostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    enctype = "multipart/form-data"

class BlogUpateView(UpdateView):
    model=Post
    template_name = "blog/post_edit.html"
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    enctype = "multipart/form-data"

class BlogDeleteView(DeleteView):
    model=Post
    template_name="blog/post_delete.html"
    success_url=reverse_lazy('index')