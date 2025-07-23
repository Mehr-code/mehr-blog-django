from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("name", "email", "comment")

        # For styling the comment's form
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "comment": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your comment"}
            ),
        }
