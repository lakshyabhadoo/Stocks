from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Your Title'}))
    video_link = forms.CharField(max_length=100)
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      'placeholder': 'Your Description',
                                      'class': 'new-class-name two',
                                      'id': 'my-id-for-textarea',
                                      'rows': 5,
                                      'cols': 50
                                  }
                                  )
                                  )


    class Meta:
        model = Stock
        fields = [
            'title',
            'video_link',
            'description',
        ]