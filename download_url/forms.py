from django import forms
from .models import Post, Channel, Senf, SaleType

class Channel_form(forms.ModelForm):
    senf = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Senf.objects.all())
    saletype = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=SaleType.objects.all())

    class Meta:

        model = Channel
        fields = ['phone', 'chat_username', 'chat_title', 'senf', 'saletype']

    # def __init__(self, *args, **kwargs):
    #     super(Channel_form, self).__init__(*args, **kwargs)
    #
    #     self.fields["senf"].widget = forms.CheckboxSelectMultiple()
    #     self.fields["senf"].queryset = Channel.objects.all()
