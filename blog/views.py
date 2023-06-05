from django.shortcuts import render ,redirect , get_object_or_404
from .models import *
from .forms import BlogForm
# Create your views here.
def blog_list_view(request):
    blogs = Blog.objects.all()
    context ={ 
       "blogs"  : blogs 
    }
    return render(request , "blogs/list.html" , context) 


def blog_detail_view(request , id ):
    blog = Blog.objects.get(id=id)
    context ={
         "blog" : blog  
    }

    return render(request , "blogs/detail.html" , context)


def blog_create_view(request):
    form = BlogForm()
    

    if request.method == "POST":
        form =  BlogForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("list") 

    context ={
       "form": form
    }

    return render(request , "blogs/create.html" , context)



def blog_update_view(request, id):
    blog = get_object_or_404(Blog , id=id)
    form = BlogForm(instance=blog)
    if request.method == "POST":
        form =  BlogForm(request.POST , instance=blog )

        if form.is_valid():
            form.save()

            return redirect("list")
    context ={
       "form": form
    }

    return render(request , "blogs/update.html" , context)




 