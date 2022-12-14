from django import forms
from . models import PostBlog,Comments


class PostBlogForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ('author','title','text')

        widgets = {
        'title': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author','text')

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
