from django.forms import ModelForm
from cms.models import Member, attribute


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'div', 'sex',)


class attributeForm(ModelForm):
    class Meta:
        model = attribute
        fields = ('comment',)
