from django.shortcuts import render,redirect
from server.apps.posts.models import Post

# Create your views here.
def hello_world(request):
    return render(request,"posts/hello_world.html")

def posts_list(request, *args,**kwargs):
    text = request.GET.get("text")
    posts = Post.objects.all()
    if text:
        posts = posts.filter(content__contains=text) # 
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
def posts_update(request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        if request.method == "POST":
            
                post.title = request.POST['title']
                post.user = request.POST['user']
                post.region = request.POST['region']
                post.price=request.POST['price']
                post.content =request.POST['content']
                post.save()

            
                return redirect(f"posts/{post.id}")
        return render(request, "posts/posts_update.html",{"post":post})

#     return render(request, "posts/create.html")
def posts_delete(request,pk,*args,**kwargs):
    if request.method =="POST":
        post = Post.objects.get(id=pk)
        print(post)
        print("!!!!")
        post.delete()
    return redirect("/")