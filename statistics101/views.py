from django.shortcuts import render
from statistics101.models import Orders, Items, MetaItems
from django.views.generic import (ListView, DetailView)
from django.http import HttpResponse
import statistics101.computation_logic.dish_count as dc
from django.contrib.auth.decorators import login_required

class OrdersList(ListView):
    model = Orders

@login_required
def orders_to_html(request, report_type):
    model = Orders
    items = Items
    meta_items = MetaItems
    #request.GET.get('report_type', 'A')
    return HttpResponse(dc.common_report(model, items, meta_items, report_type))

@login_required
def orders_to_csv(request, report_type):
    model = Orders
    items = Items
    meta_items = MetaItems
    response =  HttpResponse(dc.common_report(model, items, meta_items, report_type, True),
                        content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    return response

#class MovieDetail(DetailView):
#    model = Movie

