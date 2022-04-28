from django import forms
from web import models
from web.forms.Bootstrap import BootStrapForm


class WikiModelForm(BootStrapForm,forms.ModelForm):

    class Meta:
        model=models.Wiki
        fields=['title','content','parent']