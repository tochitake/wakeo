from django.forms import ModelForm
from cms.models import Member, attribute, Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ('name', 'memo',)


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'div', 'sex',)


class attributeForm(ModelForm):
    class Meta:
        model = attribute
        fields = ('comment',)
