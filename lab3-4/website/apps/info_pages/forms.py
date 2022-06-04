from django import forms
from django.shortcuts import render

from .models import Comment, Post


# Create your views here.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "text")

        widgets = {
            "title": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(
                attrs={"class": "editable medium-editor-textarea postclass"}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "text")

        widgets = {
            "author": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea"}),
        }
