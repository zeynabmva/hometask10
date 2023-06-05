from django import forms
from .models import Blog

# class BlogForm(forms.Form):
#     author = forms.CharField(max_length=20)
#     title =forms.CharField(max_length=20)
#     # content = forms.Textarea()
#     # created_date = forms.DateTimeField(auto_now_add=True)
#     # updated_date = forms.DateTimeField(auto_now=True)



class BlogForm(forms.ModelForm):
    class Meta :
        model = Blog
        fields= ("title" , "author" , "content")
