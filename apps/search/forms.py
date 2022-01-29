from django import forms
from search.models import *
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class UsersForm(forms.Form):
    class Meta:
        model = Users
        fields = ["first_name", "last_name", "gender", "image", "sport"]
    
    def clean(self):
        super(UsersForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        image = self.cleaned_data.get('image')

        if len(first_name)<1:
            self.errors['first_name'] = self.error_class(["First name cannot be empty"])
        elif len(first_name)<2:
            self.errors['first_name'] = self.error_class(["First name must contain at least two letters"])

        if len(last_name)<1:
            self.errors['last_name'] = self.error_class(["Last name cannot be empty"])
        elif len(last_name)<2:
            self.errors['last_name'] = self.error_class(["Last name must contain at least two letters"])
        
        if len(image)<1:
            self.errors['image'] = self.error_class(["Image link cannot be empty"])

        return self.cleaned_data