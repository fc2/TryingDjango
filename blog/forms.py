from django import forms
from .models import Post

class PostForm(forms.ModelForm):


#tell Django which model should be used to create the form
    class Meta:
        model = Post
        fields = ('title','text','image')
