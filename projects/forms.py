from django import forms


class NewProjectForm(forms.Form):

    ProjectName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'E.G. ',
        'id': 'ProjectName',
    }))

    StreamName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g. Bridge Creek',
        'id': 'StreamName',
    }))

    BasinName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g. John Day',
        'id': 'BasinName',
    }))

    ProjectLatitude = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g. 44.123456',
        'id': 'ProjectLatitude',
    }))

    ProjectLongitude = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'e.g. -120.123456',
        'id': 'ProjectLongitude',
    }))

    ProjectImage = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file',
        'id': 'ProjectImage',
    }))
