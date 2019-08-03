import datetime
from django.shortcuts import render
from app.settings import os, FILES_PATH

def file_list(request, date = '', year = 0, month = 0, day = 0):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

    if(date != ''):
        date_list = date.split('-')
        date_filter = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2])).timestamp()

    context = {'files': [], 'date': 0}
    files = os.listdir(path=FILES_PATH)

    for file in files:
        file_info = os.stat(FILES_PATH + '\\' + file)
        st_mtime = datetime.datetime.fromtimestamp(file_info.st_mtime).timetuple()
        st_ctime = datetime.datetime.fromtimestamp(file_info.st_ctime).timetuple()
        file_data = {
            'name': file,
            'ctime': datetime.datetime(st_ctime.tm_year, st_ctime.tm_mon, st_ctime.tm_mday, st_ctime.tm_hour, st_ctime.tm_min),
            'mtime': datetime.datetime(st_mtime.tm_year, st_mtime.tm_mon, st_mtime.tm_mday, st_mtime.tm_hour, st_mtime.tm_min)
        }
        if((date != '') and (date_filter >= file_info.st_mtime)):
            continue
        context['files'].append(file_data)
    context['date'] = datetime.datetime.now() #'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_content = ''
    for file_line in open(FILES_PATH + '\\' + name).readlines():
        file_content += file_line

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

