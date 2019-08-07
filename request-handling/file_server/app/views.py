import datetime
from django.shortcuts import render
from app.settings import os, FILES_PATH

def file_list(request, date = ''):
    template_name = 'index.html'
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:

    date_filter = None
    if(date != ''):
        date_list = date.split('-')
        date_filter = datetime.datetime(int(date_list[0]), int(date_list[1]), int(date_list[2]))

    context = {'files': [], 'date': 0}
    files = os.listdir(path=FILES_PATH)

    for file in files:
        try:
            file_info = os.stat(os.path.join(FILES_PATH, file))
            st_mtime = datetime.datetime.fromtimestamp(file_info.st_mtime).timetuple()
            st_ctime = datetime.datetime.fromtimestamp(file_info.st_ctime).timetuple()
            file_data = {
                'name': file,
                'ctime': datetime.datetime(st_ctime.tm_year, st_ctime.tm_mon, st_ctime.tm_mday, st_ctime.tm_hour, st_ctime.tm_min),
                'mtime': datetime.datetime(st_mtime.tm_year, st_mtime.tm_mon, st_mtime.tm_mday, st_mtime.tm_hour, st_mtime.tm_min)
            }

            if(date != ''):
                check_file_date = datetime.datetime(int(st_mtime.tm_year), int(st_mtime.tm_mon), int(st_mtime.tm_mday))
                print(date_filter, check_file_date)
                if (date_filter != check_file_date):
                    print('pass')
                    continue
            context['files'].append(file_data)
        except FileNotFoundError:
            pass
    if (date_filter != None):
        context['date'] = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))  # Этот параметр необязательный
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_content = ''

    if(os.path.exists(os.path.join(FILES_PATH, name))):
        for file_line in open(os.path.join(FILES_PATH, name)).readlines():
            file_content += file_line
    else:
        file_content = 'файла не существует'

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

