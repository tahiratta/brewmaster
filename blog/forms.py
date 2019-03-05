from django import forms
from blog.models import Document


# def validate_file_extension(value):
#     if not value.name.endswith('.csv') or not value.name.endswith('.xls') or not value.name.endswith('.xlsx'):
#         raise forms.ValidationError("Only CSV, XLS or XLSX file is accepted")
class DocumentForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(DocumentForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['accept'] = '.csv'
    document = forms.FileField(widget=forms.FileInput(attrs={'accept': ".csv"}))
    # document = forms.FileField(label='Select a file', validators=[validate_file_extension])

    class Meta:
        model = Document
        fields = ('document', )

class DateForm(forms.Form):
    fromDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    toDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    lDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    gDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    total = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
