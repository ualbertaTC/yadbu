from django.shortcuts import render
from django.http import HttpResponse
from index.models import *

column_dict = {
    "first_name" : Identity,
    "last_name" : Identity,
    "patient_number" : Identity,
    "age" : Attributes,
    "weight" : Attributes
}

def index_view(request):
    return render(request, 'index/index.html', {})

def columns(request):
    column_header = request.GET.get('column_header','')
    value = request.GET.get('value', '')
    list_of_columns = request.GET.get('list_of_columns','')
    column_header = "age"
    value =  "10"
    list_of_columns = "first_name, last_name"
    list_of_columns = [i.strip() for i in list_of_columns.split(",")] #list of columns is comma separated string
    table_set = set(column_dict[i] for i in list_of_columns) #make list of only unique table names
    table_values_list = []
    for i in table_set:
        table_values_list.append([j for j in list_of_columns if column_dict[j] == i]) 
        #for each unique table name, appending with column from corresponding table name, list of lists
    tmp_dict = {}
    tmp_dict.update(locals())
    tmp_dict.update(globals())
    exec("table_names = column_dict[column_header].objects.filter(%s=value)" % column_header, tmp_dict)
    print(tmp_dict["table_names"])
    return HttpResponse("columns works")
