from django import forms
from .models import Book

class CreateBookForm (forms.ModelForm):
    published_date = forms.DateField(widget=forms.DateInput(attrs={
        "type":"date", "name":"published_date"
    }))
    class Meta:
        model = Book
        fields = ['title','isbn','author','genre','published_date']

    def clean_title(self):
        clean_my_title = self.cleaned_data.get("title")
        #if clean_my_title:
        proper_title = clean_my_title.title()
        if Book.objects.filter(title=proper_title).exists():
            raise forms.ValidationError("This title already exists, choose a different title")
        return proper_title

class UpdateBookForm (forms.ModelForm):
    published_date = forms.DateField(widget=forms.DateInput(attrs={
            "type":"date", "name":"published_date"
        }))
    class Meta:
        model = Book
        fields = ['title','isbn','author','genre','published_date']


