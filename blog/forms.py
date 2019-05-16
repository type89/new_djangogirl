from django import forms
from .models import Post
from taggit.models import Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class TagForm(forms.ModelForm):
    taglist = Tag.objects.all()
    search_tag = forms.ChoiceField(label='タグ', choices=taglist)
