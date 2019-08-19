from django.shortcuts import render

import csv
from app.settings import INFLATION_RUSSIA_CSV


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}

    with open(INFLATION_RUSSIA_CSV, 'r', encoding='utf-8') as file_csv:
        reader = csv.reader(file_csv)
        context['title'] = next(file_csv, [])[:-1].split(';')
        context['years'] = []
        for row in reader:
            year_data = []
            for item in row[0].split(';'):
                if (item != ''):
                    year_data.append(item)
                else:
                    year_data.append('---')
            context['years'].append(year_data)
    return render(request, template_name, context)