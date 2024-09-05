from django import forms
from .models import Post,Category

cats=Category.objects.all().values_list('name','name')

choice_list=[]

for item in cats:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','tag','author','category','body')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            #'blog_datetime': forms.TextInput(attrs={'class':'form-control'}),
            #'thumbnail': forms.TextInput(attrs={'class':'form-control'}),
            

        }