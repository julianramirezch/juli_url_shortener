from django import forms
from .validators import validate_url, validator_dot_com


class SubmitUrlForm(forms.Form):
    """ Class Forms validations"""
    url = forms.CharField(
        label='', 
        validators=[validate_url],
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Long URL',
                'class': 'form-control'
                }
        )
        )

    def clean_url(self):
        url = self.cleaned_data['url']
        if 'http' in url:
            return url
        else:
            return 'http://' + url

"""
        def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        # url = cleaned_data['url']
        # print(url)

        def clean_url(self):
        url = self.cleaned_data['url']
        print('este {}'.format(url))
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError('Invalid URL for this field')
        return url """
