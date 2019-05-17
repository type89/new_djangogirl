from django import forms
from .models import Post
from taggit.models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class TagForm(forms.Form):
    taglist = forms.ModelChoiceField(label='tag',queryset=Tag.objects.all())
