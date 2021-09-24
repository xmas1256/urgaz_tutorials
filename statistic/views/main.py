from os import remove
from statistic.models import Report, Stanok, Worker
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def main_menu(request):
    return render(request, 'views/main_menu.html')

@login_required
def workers_all(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'views/workers_all.html', context)

@login_required
def stanoks_all(request):
    query = Stanok.objects.all()
    context = {'stanoks': query}
    return render(request, 'views/stanoks_all.html', context)


# @login_required
# def reports_all(request):
#     query = Report.objects.all()
#     context = {'reports': query}
#     return render(request, 'views/reports_all.html', context)


@login_required
def reports_all(request, st, year, month, day):
    obj = Report.objects.all().order_by('-date', 'stanok__number', 'value')
    
    if year != 0:
        obj = obj.filter(date__year=year)
    if month != 0:
        obj = obj.filter(date__month=month)
    if day != 0:
        obj = obj.filter(date__day=day)
    if st != 'Jami':
        obj = obj.filter(stanok__number=st)
        
    values = []
    for i in obj:
        values.append(int(i.value) + int(i.value2) + int(i.value3))

    context = {'reports': obj, 'year': year, 'month': month, 'day': day, 'st': st, 'values': values}
    context['years'] = ['2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027']
    context['months'] = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    context['days'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    
    context['stanoks'] = Stanok.objects.all().order_by('number')
    # context['path'] = ps
    
    return render(request, 'views/reports_all.html', context)

def custom_sort(t):
    return t[1]

def statistic_menu(request, smena):
    current_time = datetime.now()
    values_list = []
    for s in Stanok.objects.all():
        summary = 0
        for r in Report.objects.filter(stanok__number=s.number, date__month=current_time.month, date__year=current_time.year):
            # def value_to_per(value):
            #     per = round(((float(value)/float(s.norma_value))*100), 2)
                # return per
            if smena == 1:
                summary += int(r.value)
            elif smena == 2:
                summary += int(r.value2)
            elif smena == 3:
                summary += int(r.value3)
        summary_percent = round(((float(summary)/(float(s.norma_value)*current_time.day))*100), 2)

        values_list.append(['{} (st {})'.format(s.title, str(s.number)), summary_percent])
    
    values_list.sort(key=custom_sort, reverse=True)
    hundred_percent = values_list[0][1]
    
    result = []
    for i in values_list:
        height = round((((i[1] / hundred_percent) * 100) / 2.5), 1)
        i.append(height)
        i.append(50-height)
    months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']

    if smena == 3:
        next_page_smena = 1
    else:
        next_page_smena = smena + 1
    context = {'values': values_list, 'current_month': months[current_time.month-1], 'next_page_smena': next_page_smena, 'smena': smena}
    
    return render(request, 'views/statistic.html', context)


def custom_sort2(t):
    return t[6]

def statistic_table(request):
    current_time = datetime.now()
    values_list = []
    for s in Stanok.objects.all():
        summary1 = 0
        summary2 = 0
        summary3 = 0
        for r in Report.objects.filter(stanok__number=s.number, date__month=current_time.month, date__year=current_time.year):
            # def value_to_per(value):
            #     per = round(((float(value)/float(s.norma_value))*100), 2)
                # return per
            
            summary1 += int(r.value)    
            summary2 += int(r.value2)
            summary3 += int(r.value3)
        summary = summary1 + summary2 + summary3
        summary_percent = round(((float(summary)/(float(s.norma_value)*current_time.day))*100), 2)
        norma_atqi = int(s.norma_value)*current_time.day
        stanok_title = '{}. {}'.format(str(s.number), s.title)
        values_list.append([stanok_title, norma_atqi, summary1, summary2, summary3, summary ,summary_percent])
    months = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
    values_list.sort(key=custom_sort2, reverse=True)
    context = {'values': values_list, 'current_month': months[current_time.month-1]}
    return render(request, 'views/statistic_table.html', context)