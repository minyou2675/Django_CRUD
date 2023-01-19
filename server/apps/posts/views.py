from django.shortcuts import render,redirect
from server.apps.posts.models import Idea,Tool
from django.http.request import HttpRequest

# Create your views here.

def idea_list(request:HttpRequest):
    ideas = Idea.objects.all()
    search_mode = request.GET['search_,mode']
    if search_mode:
        ideas = ideas.filter().order_by
    return render(request,"idea/idea_list.html",{"ideas":ideas})

def idea_create(request=HttpRequest):
    if request.method == "POST":
        Idea.objects.create(
            name=request.POST['name'],
            image=request.FILES['image'],
            description = request.POST['description'],
            interest = request.POST['interest'],
            devtool = request.POST['devtool']
        )
        return redirect("/")    
    return render(request, "idea/idea_create.html")

def idea_detail(request,pk):
    idea = Idea.objects.get(pk=pk)
    return render(request,"idea/idea_detail.html",{"idea" : idea})

def idea_update(request,pk):
    idea = Idea.objects.all().get(pk=pk)
    if request.method == "POST":
        idea.name = request.POST['name']
        idea.image = request.FILES['image']
        idea.description = request.POST['description']
        idea.interest = request.POST['interest']
        idea.devtool = request.POST['devtool']
        return redirect(f"idea/{idea.pk}")
    return render(request,"idea/idea_update.html",{"idea" : idea})

def idea_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("/")

def tool_list(request):
    tools = Tool.objects.all()
    return render(request,"idea/idea_list.html",{"tools":tools})

def tool_create(request):
    if request.method == "POST":
        Tool.objects.create(
            name=request.POST['name'],
            kind=request.POST['kind'],
            description = request.POST['description'],
        )
        return redirect("/")    
    return render(request, "tool/tool_create.html")

def tool_detail(request,pk):
    tool = Tool.objects.all().get(pk=pk)
    return render(request,"tool/tool.html",{"tool":tool})

def tool_update(request,pk):
    tool = Tool.objects.all().get(pk=pk)
    if request.method == "POST":
        tool.name = request.POST['name']
        tool.kind = request.POST['kind']
        tool.description = request.POST['description']
        tool.save()  
        return redirect(f"idea/{tool.pk}")
    return render(request,"idea/idea_update.html",{"tool" : tool})
