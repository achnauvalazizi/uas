from django.forms import ModelForm
from django import forms
from about.models import 

class FormBuku(ModelForm):
    class Meta :
        model = about
        fields = '__all__'
# fields = ['judul'] Memilih Untuk ditampilkan
        widgets = {
        'judul' : forms.TextInput({'class':'form-control'}),
        }