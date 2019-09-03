from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_rate(self):
        rate = self.cleaned_data.get('rate')
        if not rate  or rate  < 0:
            raise forms.ValidationError("Процентная ставка не может быть отрицательной")
        return rate


    def clean_months_count(self):
        months_count = self.cleaned_data.get('months_count')
        if not months_count or months_count  < 0:
            raise forms.ValidationError("Необходимо указать количество месяцев")
        return months_count

    def clean(self):
        return self.cleaned_data