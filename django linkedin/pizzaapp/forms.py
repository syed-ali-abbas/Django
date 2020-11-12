from django import forms
from .models import Pizza, PizzaSize

# class PizzaForm(forms.Form):
    # topping1 = forms.CharField(max_length=100)
    # topping2 = forms.CharField(max_length=100)
    # size = forms.ChoiceField(choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=PizzaSize.objects,empty_label=None,widget=forms.RadioSelect)

    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
        labels ={'topping1': 'Topping 1','topping2': 'Topping 2','size':'Size'}
        # widgets={
        #     'size':forms.CheckboxSelectMultiple,
        # }



class MultiplePizzas(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=6)