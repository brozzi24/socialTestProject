from django import forms
from .models import Post, Comment


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text"]


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {"text": forms.Textarea(attrs={"rows": 4, "cols": 30})}
