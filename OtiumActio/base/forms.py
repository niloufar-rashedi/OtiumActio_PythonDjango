from django.forms import ModelForm
from .models import Category, Activity

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'