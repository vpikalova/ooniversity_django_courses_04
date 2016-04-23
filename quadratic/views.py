# -*- coding: utf-8 -*-
from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
        
    disc = {}
    text_result = {}

    if request.method == "GET":
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            disc['message'] = "Дискриминант: "
            disc['value'] = b**2-4*a*c

            if disc['value'] < 0:
                text_result['message'] = u"Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif disc['value'] == 0:
                x = (-b + disc['value'] ** (1/2.0)) / 2*a
                text_result['message'] = u"Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "
                text_result['value'] = x
            else:
                x1 = (-b + disc['value'] ** (1/2.0)) / 2*a
                x2 = (-b - disc['value'] ** (1/2.0)) / 2*a
                text_result['message'] = u"Квадратное уравнение имеет два действительных корня: " 
                text_result['value'] = u"x1 = %.1f, x2 = %.1f" % (x1, x2)
    else:
        form = QuadraticForm()
    
    out_result =  context = {"disc":disc, "text_result":text_result, "form":form}
    
    return render(request,'quadratic/results.html', out_result)
