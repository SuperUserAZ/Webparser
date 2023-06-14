from django.shortcuts import render
from .parsesite import parse_trendyol, get_card_count, close_driver

def main_page(request):
    return render(request, 'main/index.html')

def parse_page(request):
    parse_trendyol()
    card_count = get_card_count()
    if card_count == 0:
        close_driver()
        return render(request, 'main/finished.html')
    else:
        return render(request, 'main/wait.html', {'card_count': card_count})



""" 
from django.http import JsonResponse

def get_card_count_ajax(request):
    card_count = get_card_count()
    data = {'card_count': card_count}
    return JsonResponse(data)


 """


""" 
def parse_page(request):
    parse_trendyol()
    return render(request, 'main/wait.html')
    

 """

""" 
from django.shortcuts import render
from .parsesite import parse_trendyol
from django.http import HttpResponse
from mycelery import app

# Используйте декоратор task для определения задачи Celery
@app.task
def run_parser():
    parse_trendyol()

def run_parser_view(request):
    # Запуск парсера как задачи Celery
    run_parser.delay()
    return render(request, 'main/index.html')



 """
