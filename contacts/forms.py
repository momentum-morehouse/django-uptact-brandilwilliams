from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'birthday'.
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
      ]


        widgets = {
          "birthday": 
              forms.DateInput{
              format=['%m/%d/%Y'], 
              attrs= (
                'class':'form-control', 
                'placeholder' :'Select a date',
                'type': 'date'
              }),
      }

class NoteForm(forms,Form|:
    class Meta:
        model = Note 
        fields =(
            "note"
        )
        