from django.contrib.auth.models import User
import blog
from django.shortcuts import redirect, render
from . models import BlogPost, UserProfile
from .forms import BlogPostForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs = BlogPost.objects.all()[:4]
    latest = BlogPost.objects.all().order_by('-created_at')[:3]
    context={
        "blogs": blogs,
        "latest": latest
    }
    return render(request, "blog/index.html", context)

def allblog(request):
    search_query = ''
    if request.GET.get("search"):
        search_query = request.GET.get("search")
    blogs = BlogPost.objects.filter(title__icontains=search_query).order_by("-created_at")
    context={
        "blogs": blogs,
        "search_query": search_query
    }
    return render(request, "blog/blog.html", context)


def post(request, pk):
    post = BlogPost.objects.get(id=pk)
    context={
        "post": post
    }
    return render(request, "blog/post.html", context)


@login_required(login_url='loginuserprofile')
def createpost(request):
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            print(f"from form {request.user}")
            instance = form.save(commit=False)
            instance.author = request.user.profile
            instance.save()
            return redirect("allblog")
    context = {"form":form}
    return render(request, "blog/post_form.html", context)

@login_required(login_url='loginuserprofile')
def updatepost(request, pk):
    post= BlogPost.objects.get(id=pk)
    form = BlogPostForm(instance=post)
    if request.method =="POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("allblog")
    context = {"form":form}
    return render(request, "blog/post_form.html", context)

@login_required(login_url='loginuserprofile')
def deletepost(request, pk):
    post = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("allblog")
    context = {"post":post}
    return render(request, "blog/delete.html", context)

@login_required(login_url='loginuserprofile')
def userProfile(request,pk):
    userprofile = UserProfile.objects.get(id=pk)
    posts = BlogPost.objects.filter(author=userprofile).order_by("-created_at")
    context = {
        "userprofile":userprofile,
        "posts": posts
    }
    return render(request, "blog/profile.html", context)

@login_required(login_url='loginuserprofile')
def editUserProfile(request,pk):
    userprofile = UserProfile.objects.get(id=pk)
    posts = BlogPost.objects.filter(author=userprofile).order_by("-created_at")
    context = {
        "userprofile":userprofile,
        "posts": posts
    }
    return render(request, "blog/profile_edit.html", context)

def loginUserProfile(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("allblog")
        # Redirect to a success page.
        ...
    else:
        pass
    return render(request, "blog/login.html")


@login_required(login_url='loginuserprofile')
def logoutUserProfile(request):
    logout(request)
    return redirect("loginuserprofile")


def editProfile(request, pk):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            custom_form = profile_form.save(commit=False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('blog/profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.userprofile)
        args = {}
        args['form'] = user_form
        args['profile_form'] = profile_form
        return render(request, "blog/profile_edit_test.html", args)