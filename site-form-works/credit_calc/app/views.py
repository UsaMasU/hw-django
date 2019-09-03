from django.shortcuts import render
from .forms import CalcForm

def calc_view(request):
    template = "app/calc.html"

    get_cost = request.GET

    if len(get_cost) > 0:
       common_result = (float(get_cost['initial_fee']) + float(get_cost['initial_fee']) * float(get_cost['rate']) / float(get_cost['months_count']))
       result = common_result  / 12
       result = '{:.3f}'.format(result)
       common_result = '{:.2f}'.format(common_result)

       form = CalcForm(request.GET)
       if form.is_valid():
           context = {
               'form': form,
               'result': result,
               'common_result': common_result
           }
       else:
           context = {
               'form': form,
               'result': None,
               'common_result': None
           }
       return render(request, template, context)
    else:
        form = CalcForm
        context = {
            'form': form
        }
        return render(request, template, context)
