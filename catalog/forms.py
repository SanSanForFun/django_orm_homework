from django.forms import ModelForm
from .models import Products
from django.core.exceptions import ValidationError
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'image', 'category', 'price']
        exclude = ['created_at', 'updated_at']

    def clean_name(self):
        forbidden_words = (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name:
            for word in forbidden_words:
                if word.lower() in name.lower():
                    raise forms.ValidationError(f'Название содержит запрещенное слово "{word}"')

    def clean_description(self):
        forbidden_words = (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")
        cleaned_data = super().clean()
        description = cleaned_data.get('description')

        if description:
            for word in forbidden_words:
                if word.lower() in description.lower():
                    raise forms.ValidationError(f'Название содержит запрещенное слово "{word}"')

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price < 0:
            self.add_error('price', 'Цена не может быть отрицательной')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Изображение'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })
