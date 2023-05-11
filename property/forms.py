from django.forms import ModelForm

from properties.models import Property

class PropertyForm(ModelForm):

    class Meta:
        model = Property
        fields = '__all__'