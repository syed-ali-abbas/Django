from django.shortcuts import render
from .forms import PersonCreationForm
from .models import Person, City, Country



def HomePageView(request):
    form = PersonCreationForm
    return render(request,'index.html',{'form':form})
    


def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    data={
    'cities': cities
    }
    return render(request, 'city_dropdown_list_options.html', data)

    













