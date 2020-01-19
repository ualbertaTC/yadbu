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
    head, data = columns(request)
    return render(request, 'index/index.html', {"table_head" : head, "table_data" : data})
    #passing dictionary to the render. it is implemented in index.html

def columns(request):
    column_header = request.GET.get('column_header','')
    value = request.GET.get('value', '')
    list_of_columns = request.GET.get('list_of_columns','')
    
    if (column_header == "" or value == "" or list_of_columns == ""):
        return [], [[]]

    list_of_columns = [i.strip() for i in list_of_columns.split(",")] #list of columns is comma separated string so strip and split by comma
    table_set = set(column_dict[i] for i in list_of_columns) #set() makes a list of only unique table names using generator
    table_values_list = []
    for i in table_set:
        table_values_list.append([j for j in list_of_columns if column_dict[j] == i]) 
        #for each unique table name, append with column from corresponding table name. Would start new list for next table name
    patient_number_sets = []
    for i,v in zip(column_header.split(","), value.split(",")):
        table_names = column_dict[i].objects.filter(**{i:v}) #key word argument unpacking - interprets column_header as "age"
        queryS = table_names.values_list('patient_number') #find patient number of those who match the query above
        patient_number_sets.append(set(queryS))
    
    queryS = patient_number_sets[0]
    if (len(patient_number_sets) > 1):
        queryS = queryS.intersection(*patient_number_sets[1:])
    queryS = [j for i in queryS for j in i]
    
    result_list = []
    for i in table_values_list:
        result_list.append(list(column_dict[i[0]].objects.filter(patient_number__in=queryS).values_list(*i))) 
        #for each table name, filter the corresponding attribute by inserting first element into dictionary
        #__in allows to return multiple values as iterated over provided query (ex. all Identity values of patient #6)
        #values_list allows() to look at value of only variables you want. * sends inputs one at a time
    output_data = [[k for j in i for k in j] for i in zip(*result_list)]
    output_columns = [j for i in table_values_list for j in i]
    column_indexs = [output_columns.index(i) for i in list_of_columns]
    output_data = [[i[j] for j in column_indexs] for i in output_data]

    return list_of_columns, output_data
