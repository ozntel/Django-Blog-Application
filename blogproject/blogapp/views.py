from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import Post, Comment, Category
from django.contrib.auth import authenticate, login, logout

def MainView(request):
    posts = Post.objects.filter(visible=True)
    categories = Category.objects.all()
    category = ''
    if request.method == 'GET':
        if 'category' in request.GET:
            category = request.GET['category']
            if category != 'All':
                posts = Post.objects.filter(category__name=category, visible=True)
    ctx = {'posts' : posts.order_by('-post_date'), 'category' : category, 'categories' : categories}
    return render(request, 'blogapp/mainview.html', ctx)

def PostDetailView(request, pk):
    post = Post.objects.get(pk=pk)
    if post.visible == True or request.user.is_superuser or post.author == request.user:
        if request.method == 'POST':
            name = request.POST.get('name')
            comment = request.POST.get('comment')
            comment = Comment(body=comment, author=name, post=post, visible=False)
            comment.save()
            messages.info(request, 'Thank you for your comment. It is sent for review and will appear under the post very soon.')
        comments = Comment.objects.filter(post=post, visible=True)
        ctx = {'post': post, 'comments' : comments}
        return render(request, 'blogapp/postview.html', ctx)
    else:
        return redirect('compapp:NoAccess')

def LikePost(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes = post.likes + 1
    post.save()
    messages.info(request, 'I\'m glad you liked the article. Thank you for reading!')
    return redirect('blog:PostDetailView', pk)

@method_decorator(login_required(), 'dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'snippet', 'category']
    success_url = reverse_lazy('blog:MainView')
    def form_valid(self, form):
        object = form.save(commit=False)
        object.author = self.request.user
        object.save()
        post = Post.objects.get(pk=object.pk)
        messages.info(self.request, 'Your post is saved and sent for review. Once it is approved, it will be published.')
        return super(PostCreateView, self).form_valid(form)

@method_decorator(login_required(), 'dispatch')
class PostEditView(UpdateView):
    model = Post
    fields = ['title', 'body', 'snippet', 'category']
    success_url = reverse_lazy('blog:MainView')
    def get_queryset(self):
        qs = super(PostEditView, self).get_queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=self.request.user, locked=False)

@login_required()
def MyArticlesView(request):
    posts = Post.objects.filter(author=request.user)
    categories = []
    for post in posts:
        if not post.category in categories:
            categories.append(post.category)
    category = ''
    if request.method == 'GET':
        if 'category' in request.GET:
            category = request.GET['category']
            if category != 'All':
                posts = posts.filter(category__name=category)
    ctx = {'posts' : posts.order_by('-post_date'), 'category' : category, 'categories' : categories, 
        'view' : 'MyArticlesView'}
    return render(request, 'blogapp/mainview.html', ctx)

def NoAccess(request):
    return render(request, 'blogapp/noaccess.html')

@login_required()
@user_passes_test(lambda u:u.is_superuser, login_url='blog:NoAccess')
def ApprovePost(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.visible = True
        post.locked = True
        post.save()
        messages.info(request, 'Post is approved and visible in Ozan.pl blog page.')
        return redirect('blog:MainView')
    return render(request, 'blogapp/postapprove.html', {'post' : post})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, 'You logged in successfully...')
            return redirect('blog:MainView')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    ctx = {}
    return render(request, 'login.html', ctx)

def LogoutView(request):
    messages.info(request, 'Successfully logged out...')
    logout(request)
    return redirect('blog:MainView')