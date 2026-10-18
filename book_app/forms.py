from django import forms
from .models import Book,BookRequest

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

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ["book","date_of_request","date_of_return"] # other fields from models are no need as they're automatic

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        date=["date_of_request","date_of_return"]
        for i in date:

            self.fields[i].widget=forms.DateInput(
                    attrs = {
                        "type":"date"
                    }
                        
                )
        self.fields["book"].queryset=Book.objects.filter(status="av")   #showing only available books when create a book request 


    def clean(self):
        cleaned_data=super().clean()
        request_date=cleaned_data.get("date_of_request")
        return_date=cleaned_data.get("date_of_return")
        if request_date and return_date:
            if return_date < request_date:
                raise forms.ValidationError(
                    "The return date cannot be earlier the request date."
                )
        #return request_date,return_date   
        return cleaned_data 

'''
    self.fields["date_of_request"].widget=forms.DateInput(
        attrs={
            "type":"date"
        }
            
    )
    self.fields["date_of_return"].widget=forms.DateInput(
            attrs={
                "type":"date"
            }
                
        )
    '''
