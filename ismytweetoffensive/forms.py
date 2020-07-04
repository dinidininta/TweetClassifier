from django import forms

class TweetForm(forms.Form):
  tweet = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={'placeholder': 'Type your tweet here', 'class': 'textfield'}), 
    max_length=280)