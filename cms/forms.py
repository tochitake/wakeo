from django import forms
from django.core.files.storage import default_storage
from .widgets import FileUploadableTextArea

from django.forms import ModelForm
from cms.models import Member, attribute, Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ('name', 'memo',)


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'div', 'sex', 'team')


class attributeForm(ModelForm):
    class Meta:
        model = attribute
        fields = ('comment',)


#class PostForm(forms.ModelForm):

#    class Meta:
#        model = Post
#        fields = '__all__'
#        widgets = {
#            'text': FileUploadFormTextArea,
#        }

class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子「.csv」のファイルをアップロードしてください。')



class FileUploadForm(forms.Form):
    file = forms.FileField()

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        file_url = default_storage.url(file_name)
        return file_url