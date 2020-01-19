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

    return render(request, 'index/index.html', {"table_head" : ["age", "weight"], "table_data" : [["12","69"], ["18", "72"]]})
    #passing dictionary to the render. it is implemented in index.html

def columns(request):
    column_header = request.GET.get('column_header','')
    value = request.GET.get('value', '')
    list_of_columns = request.GET.get('list_of_columns','')
    
    column_header = "age"
    value =  "12"
    list_of_columns = "first_name, last_name" #as if entered by user

    list_of_columns = [i.strip() for i in list_of_columns.split(",")] #list of columns is comma separated string so strip and split by comma
    table_set = set(column_dict[i] for i in list_of_columns) #set() makes a list of only unique table names using generator
    table_values_list = []
    for i in table_set:
        table_values_list.append([j for j in list_of_columns if column_dict[j] == i]) 
        #for each unique table name, append with column from corresponding table name, list of lists
    table_names = column_dict[column_header].objects.filter(**{column_header:value}) #key word argument unpacking
    
    return HttpResponse("columns works")
