from django import forms
from committee.models import Applicant, Committeeman


class ApplicantForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Applicant
        fields = '__all__'

class CommitteemanForm(forms.ModelForm):

    class Meta:
        model = Committeeman
        fields = '__all__'