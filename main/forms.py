from django.forms import ModelForm
from . models import assessment

class AssForm(ModelForm):
    class Meta:
        model = assessment
        fields = "__all__"
        exclude = ['course', 'usernames']