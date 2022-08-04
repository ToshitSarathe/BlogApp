from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from blogApp.models import PostBlog,Comments
from blogApp.forms import PostBlogForm,CommentsForm
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = PostBlog

    def get_queryset(self):
        return PostBlog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = PostBlog

class CreatePostView(LoginRequiredMixin,CreateView):
     #success_url = 'blogApp/postblog_detail.html'
     login_url = '/login/'
     redirect_filed_name = 'blogApp/postblog_detail.html'
     form_class = PostBlogForm
     model = PostBlog



class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_filed_name = 'blogApp/postblog_detail.html'
    form_class = PostBlogForm
    model = PostBlog
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = PostBlog
    success_url =reverse_lazy('blogApp:blog_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_filed_name = 'blogApp/post_list.html'
    model = PostBlog

    def get_queryset(self):
        return PostBlog.objects.filter(published_date__isnull=True).order_by('create_date')


def post_publish(request,pk):
    post = get_object_or_404(PostBlog,pk=pk)
    post.publish()
    return redirect('blogApp:blog_detail',pk=pk)
###########################
#For comments part
###########################
#@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(PostBlog,pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogApp:blog_detail',pk=post.pk)
    else:
        form = CommentsForm()
        return render(request,'blogApp/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('blogApp:blog_detail',pk=comment.post.pk)
@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blogApp:blog_detail',pk=post_pk)
