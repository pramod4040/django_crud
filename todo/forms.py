# from django.forms import ModelForm
from django import forms
from todo.models import Tasks
from bootstrap_datepicker_plus import DateTimePickerInput
# from django import widgets

class TodoForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'start_date' : DateTimePickerInput(),
            'end_date' : DateTimePickerInput(),
        }

    name =  forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=40, widget=forms.Textarea(attrs={'class':'form-control'}))
    CHOICES = (('random', 'Random'), ('programming', 'Programming'), ('wisdom_learning', 'Wisdom/Learning'))
    task_type = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    # start_date = DateTimePickerInput()
    # end_date = DateTimePickerInput()
        # widgets = {
        #     'name': forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'})),
        #     'description' : forms.CharField(widget=forms.Textarea),
        # }
    # name = forms.CharField(max_length=100)
    # description=forms.CharField(widget=forms.Textarea())
