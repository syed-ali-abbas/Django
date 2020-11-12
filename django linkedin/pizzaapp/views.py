from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzas
from django.forms import formset_factory

def home(request):
    return render(request,'home.html')


def pizzas(request):
    number_of_pizza = 2
    filled_multiple_pizza_form = MultiplePizzas(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizza=filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm,extra=number_of_pizza)
    formset = PizzaFormSet()
    if request.method=='POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():

            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note='Pizzas have been Ordered'
        else:
            note='Order Not Created Please Try again'
        return render(request, 'pizzas.html', {'formset': formset, 'note':note})
    else:
        return render(request, 'pizzas.html', {'formset': formset})










def order(request):
    multiple_form = MultiplePizzas()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note='Thanks for Ordering %s %s and %s Pizza is on its way'%(filled_form.cleaned_data['size'],
                                                                         filled_form.cleaned_data['topping1'],
                                                                         filled_form.cleaned_data['topping2'],)
            new_form = PizzaForm
            return render(request, 'order.html', {'pizzaForm': new_form,'note':note, 'multiple_form':multiple_form})

    else:
        form = PizzaForm
        return render(request,'order.html',{'pizzaForm':form,'multiple_form':multiple_form})
