from django.contrib import admin

from .models import Student, Teacher


class MembershipInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    inlines = [MembershipInline, ]


class StudentAdmin(admin.ModelAdmin):
    inlines = [MembershipInline, ]
    exclude = ('teachers',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)



# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     pass
