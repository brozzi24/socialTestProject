from django import forms
from .models import Post, Comment


class roomForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['text']

# test
class roomForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['']