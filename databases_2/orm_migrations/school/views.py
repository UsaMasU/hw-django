from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'

    students = Student.objects.prefetch_related('teachers').order_by('group')
    #students = Student.objects.all().order_by('group')
    context = {
        'object_list': students
    }

    for student in students:
        print('student:', student.name)
        for teacher in student.teachers.all():
            print('teacher:', teacher.name)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
