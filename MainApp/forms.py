from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the blog'}),
            'content': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Content of the blog'}),
        }