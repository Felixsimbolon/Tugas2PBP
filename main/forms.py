from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["item","picture_link", "price", "description"]
    def clean_item(self):
        item = self.cleaned_data["item"]
        return strip_tags(item)
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)