from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='Name',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='Email',\
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender',required=False,\
        widget=forms.CheckboxInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='Age',\
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label='Birth',\
        widget=forms.DateInput(attrs={'class':'form-control'}))    
