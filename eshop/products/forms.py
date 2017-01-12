# coding=utf-8
from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    comment = forms.CharField(label='Comment', widget=forms.Textarea)

    def clean_comment(self):
        if "abc" in self.cleaned_data['comment']:
            raise forms.ValidationError('abc prohibited')
        return self.cleaned_data['comment']


class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('product', )
