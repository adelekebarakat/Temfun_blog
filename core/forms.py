from django import forms
from .models import Post, Category, Comment





choices = Category.objects.all().values_list('title_cat', 'title_cat')
if choices:
    choice_list = []
    for item in choices:
        choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'intro', 'category', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control',}),
            'intro': forms.Textarea(attrs={'class': 'form-control',}),
            'body': forms.Textarea(attrs={'class': 'form-control', }),
            
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','intro', 'body', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of blog'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title_tag of blog'}),
            'intro': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a short description of your oblog'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write the content of your blog here'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control',}),
            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),            
        }
