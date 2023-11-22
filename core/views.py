from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))


    context ={
        'cats': cats.title().replace('-', ' '),
        'category_post': category_post

    }
    
    return render(request, 'core/categories.html', context)


def CategoryViewList(request):
    cat_menu_list = Category.objects.all()
    context ={
        'cat_menu_list': cat_menu_list,

    }
    return render(request, 'core/category_list.html', context)






class Home(ListView):
    model = Post
    template_name = 'core/index.html'

    def get_context_data(self, *arg, **kwargs):
        cat_menu = Category.objects.all()
        context  = super(Home, self).get_context_data(*arg, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Detail(DetailView):
    model = Post
    template_name = 'core/detail.html'


    def get_context_data(self, *arg, **kwargs):
        cat_menu = Category.objects.all()
        context  = super(Detail, self).get_context_data(*arg, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    



class Createblog(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/create_blog.html'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *arg, **kwargs):
        cat_menu = Category.objects.all()
        context  = super(Createblog, self).get_context_data(*arg, **kwargs)
        context["cat_menu"] = cat_menu
        return context

    

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__contains = query) | Q(intro__contains = query ) | Q(body__contains = query))
    context ={
        'posts': posts,
        'query' : query
    }
    return render(request, 'core/search.html' ,context)


class AddCategory(CreateView):
    model = Category
    template_name = 'core/addcategory.html'
    fields = ['title_cat']


class Updateblog(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'core/edit.html'


class Deleteblog(DeleteView):
    model = Post
    template_name = 'core/delete.html'
    success_url = reverse_lazy('home')


class CommentSection( LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'core/addcomment.html'
    login_url = '/auth/login/'
    redirect_field_name = "redirect_to"
    

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')