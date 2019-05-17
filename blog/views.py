from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, TagForm
from taggit.models import Tag
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
#from .forms import SearchForm

#def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #taglist = Tag.objects.all()
    #for tag in taglist:
        #print(tag)
    #return render(request, 'blog/post_list.html', {'posts': posts, 'taglist': taglist})

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'Post'
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

#def post_detail(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    #return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def tagform(request):
    return HttpResponse(str(TagForm()))

#class TagSelectView(CreateView):
    #model = Tag
    #form_class = TagForm
    #template_name = "blog/form.html"
    #success_url = ""  # 成功時にリダイレクトするURL

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html',{})

def tagview(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    tag_name='django'
    tag = get_object_or_404(Tag, name=tag_name)
    print("tag --> " + str(tag))
    posts = posts.filter(tags__in=[tag])
    for item in posts:
        print("title --> " + str(item.title))
    #post = get_object_or_404(Post, pk=pk)

    #post = posts.objects.filter(field=filter_tag)
    return render(request, 'blog/tag_post_list.html', {'posts': posts})
