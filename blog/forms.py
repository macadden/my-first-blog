from django import forms

from .models import Post

class PostForm(forms.ModelForm): #Formulario

    class Meta: #Acá aclaro qué modelo (Post) hay que usar para crear el formulario
        model = Post
        fields = ('title', 'text',) #Qué campos quiero en el formulario.

        