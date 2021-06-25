from django.shortcuts import render
from django.views.generic import CreateView
from .models import Stock
from market.forms import StockForm
from django.urls import reverse_lazy
import csv
from django.shortcuts import HttpResponse
from django.utils.encoding import smart_str


# Create your views here.
class Stock_view(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'create_stock.html'
    success_url = reverse_lazy('home')


def load_stock(request):

    if request.user.is_authenticated:
        start_index = int(request.GET.get('start_index', 0))
        to_load = int(request.GET.get('to_load', 5))
        search_query = request.GET.get('search_query', None)

        stocks = Stock.objects.all()
        if search_query:
            stocks = stocks.filter(title__contains=search_query)
        stocks = stocks[:start_index + to_load]

        return render(request, 'home.html', {'stocks': stocks, "username": request.user.username,
                                             'start_index': start_index+to_load, 'to_load': to_load,
                                             'search_query': search_query})

    else:
        return render(request, "logged_out.html", {})


def get_stock(request, slug):
    s = Stock.objects.get(slug=slug)

    return render(request, 'get_stock.html', {'stock': s})


def export_stocks(request):
    fields = ['title', 'description', 'video_link']
    with open('export.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        # write your header first
        for obj in Stock.objects.all():
            row = ""
            for field in fields:
                row += getattr(obj, field) + ","
            writer.writerow(row)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    response['X-Sendfile'] = smart_str("export.csv")
    return response