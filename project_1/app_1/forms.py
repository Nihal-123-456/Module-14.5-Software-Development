from django import forms
import datetime

class form1(forms.Form):
    Name=forms.CharField(widget=forms.Textarea(attrs={'rows':1,'placeholder':'Your name'}))
    Email=forms.EmailField()
    Date_of__birth=forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}),initial=datetime.date.today)
    Age=forms.DecimalField()
    About_you=forms.CharField(widget=forms.Textarea(attrs={'rows':3}),required=False)
    OCCUPATION_CHOICES = [
    ('business', 'Business'),
    ('service', 'Service'),
    ('student', 'Student'),
]
    Your_occupation=forms.ChoiceField(choices=OCCUPATION_CHOICES,widget=forms.RadioSelect)
    KNOWING_CHOICES = [
    ('friends', 'Friends'),
    ('family', 'Family'),
    ('internet', 'Internet'),
]
    Know=forms.MultipleChoiceField(label='How did you know about us',widget=forms.CheckboxSelectMultiple,choices=KNOWING_CHOICES)
    Upload_your_photo=forms.FileField()
    Agree=forms.BooleanField(label='I agree to the terms and conditions')
    