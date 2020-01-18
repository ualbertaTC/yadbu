from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .search import search, sort
import json

def search_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term','')
        key = request.GET.get('key','')
        results = sort(key, search(key, query.lower()), query.lower())
        data = json.dumps(results)
    else:
        data = 'fail'
    type = 'application/json'
    return HttpResponse(data, type)


