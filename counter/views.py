from django.shortcuts import render

# Create your views here.


# KmDgeps/w+IBmZrDMzFy3g==FY9Re3n6fUNOZUYs

def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=5NJaf3OLtVCzHbtXEmemrzcpf1X2Oa6OBjccHaue'
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': '5NJaf3OLtVCzHbtXEmemrzcpf1X2Oa6OBjccHaue'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

