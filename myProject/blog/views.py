from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post,Category
from django.urls import reverse_lazy




class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ["-post_date"]
    
    def get_context_data(self, **kwargs):
        cat_menu =  Category.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    # Get the category object based on the category name
    category = Category.objects.get(name=cats)
    
    # Get all categories
    cats = Category.objects.all()
    
    # Filter posts based on the category object
    category_posts = Post.objects.filter(category=category)
    
    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

class AddPostView(CreateView):  
    model = Post
    template_name="add_post.html"
    fields = "__all__"

class AddCategoryView(CreateView):  
    model = Category
    template_name="add_category.html"
    fields= "__all__"

class UpdatePostView(UpdateView):  
    model = Post
    template_name="update_post.html"
    fields=['title','title_tag','body','image']
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy("home")
    