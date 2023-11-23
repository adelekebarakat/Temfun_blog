from django import forms
from .models import Post, core_category, Comment





# choices = core_category.objects.all().values_list('pk', 'title_cat')
# choices = Category.objects.all().values_list('name', 'name')
# choice_list = list(choices)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'intro', 'category', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',}),
           
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
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control',}),
            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),            
        }
