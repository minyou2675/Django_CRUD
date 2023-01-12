from django.shortcuts import render,redirect
from server.apps.posts.models import Post

# Create your views here.
def hello_world(request):
    return render(request,"posts/hello_world.html")

def posts_list(request, *args,**kwargs):
    posts = Post.objects.all()
    print({"posts" : posts})
    return render(request,"posts/posts_lists.html",{"posts" : posts})

def posts_retrieve(request,pk,*args,**kwargs):
    print("pk",pk)
    post = Post.objects.all().get(id=pk)
    return render(request,"posts/posts_retrieve.html",{"post" : post})

def posts_create(request, *args , **kwargs):
    print(request.method) #작성시
    if request.method == "POST":
        Post.objects.create(
            title=request.POST['title'],
            user=request.POST['user'],
            region=request.POST['region'],
            price=request.POST['price'],
            content=request.POST['content'],
            
        )
        return redirect("/")
    
    return render(request,"posts/posts_create.html")#첫번째

# def create(request, *args, **kwargs):
#     return render(request, "posts/create.html")
def posts_delete(request,pk,*args,**kwargs):
    if request.method =="POST":
        post = Post.objects.get(id=pk)
        print(post)
        print("!!!!")
        post.delete()
    return redirect("/")