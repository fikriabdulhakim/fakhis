from django.shortcuts import render

def home(request):
    industries = [
        'Office & Commercial Buildings','Facilities & Critical Infrastructure',
        'Hospitals & Elderly Care','Manufacturing & Plants','Open Pit & Underground'
    ]
    return render(request, 'core/home.html', {'industries': industries})
