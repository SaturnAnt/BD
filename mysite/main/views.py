from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import Well_typeForm, Area_typeForm, Column_typeForm, Cementing_typeForm, AreaFilter, WellFilter, ColumnsFilter, CementingFilter
from django.contrib import messages
from .models import Area, Well, Columns, Cementing
from django.urls import reverse_lazy


def index(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'main/contact.html')

def login(request):
    return render(request, 'main/login.html')

def mainbar(request):
    return render(request, 'main/navbar.html')

def area(request):
    area = Area.objects.order_by('-id_area')
    area_f = Area.objects.all()
    '''
    print("--------------------------")
    print(areas.query)
    '''
    paginator = Paginator(area, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'area_f' : area_f, 
        'area' : page,
        'is_paginated' : is_paginated,
        'prev_url' : prev_url,
        'next_url' : next_url,
        }    
    return render(request, 'main/area.html', context=context)

class Area_typeCreate(CreateView):
    # model = Area
    form_class = Area_typeForm
    template_name = 'main/area_create.html'
    success_url = '/area/'

class Area_typeUpdate(UpdateView):
    model = Area
    form_class = Area_typeForm
    template_name = 'main/area_update.html'
    success_url = '/area/'

class Area_typeDelete(DeleteView):
    model = Area
    template_name = 'main/area_delete.html'
    context_object_name = 'area'
    success_url = reverse_lazy('area')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(Area_typeDelete,self).form_valid(form)

def well(request):
    well = Well.objects.order_by('-id_well')
    '''
    print("--------------------------")
    print(well.query)
    '''
    paginator = Paginator(well, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'well' : page,
        'is_paginated' : is_paginated,
        'prev_url' : prev_url,
        'next_url' : next_url,
        }
    return render(request, 'main/well.html', context=context)

class Well_typeCreate(CreateView):
    # model = Area
    form_class = Well_typeForm
    template_name = 'main/well_create.html'
    success_url = '/well/'

class Well_typeUpdate(UpdateView):
    model = Well
    form_class = Well_typeForm
    template_name = 'main/well_update.html'
    success_url = '/well/'

class Well_typeDelete(DeleteView):
    model = Well
    template_name = 'main/well_delete.html'
    context_object_name = 'well'
    success_url = reverse_lazy('well')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(Well_typeDelete,self).form_valid(form)
    
def column(request):
    column = Columns.objects.order_by('-id_column')
    '''
    print("--------------------------")
    print(well.query)
    '''
    paginator = Paginator(column, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'column' : page,
        'is_paginated' : is_paginated,
        'prev_url' : prev_url,
        'next_url' : next_url,
        }
    return render(request, 'main/column.html', context=context)

class Сolumn_typeCreate(CreateView):
    # model = Area
    form_class = Column_typeForm
    template_name = 'main/column_create.html'
    success_url = '/column/'

class Сolumn_typeUpdate(UpdateView):
    model = Columns
    form_class = Column_typeForm
    template_name = 'main/column_update.html'
    success_url = '/column/'

class Сolumn_typeDelete(DeleteView):
    model = Columns
    template_name = 'main/column_delete.html'
    context_object_name = 'column'
    success_url = reverse_lazy('column')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(Сolumn_typeDelete,self).form_valid(form)
    
def cementing(request):
    cementing = Cementing.objects.order_by('-id_cementing')

    print("start-----------------------")
    print(cementing.query)
    print("end-----------------------")

    paginator = Paginator(cementing, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'cementing' : page,
        'is_paginated' : is_paginated,
        'prev_url' : prev_url,
        'next_url' : next_url,
        }
    return render(request, 'main/cementing.html', context=context)

class Cementing_typeCreate(CreateView):
    # model = Area
    form_class = Cementing_typeForm
    template_name = 'main/cementing_create.html'
    success_url = '/cementing/'

class Cementing_typeUpdate(UpdateView):
    model = Cementing
    form_class = Cementing_typeForm
    template_name = 'main/cementing_update.html'
    success_url = '/cementing/'

class Cementing_typeDelete(DeleteView):
    model = Cementing
    template_name = 'main/cementing_delete.html'
    context_object_name = 'cementing'
    success_url = reverse_lazy('cementing')
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(Cementing_typeDelete,self).form_valid(form)
    
def area_list(request):
    area_filter = AreaFilter(request.GET, queryset=Area.objects.all())
    return render(request, 'main/area_list.html', {'filter' : area_filter})

def well_list(request):
    well_filter = WellFilter(request.GET, queryset=Well.objects.all())
    return render(request, 'main/well_list.html', {'filter' : well_filter})

def column_list(request):
    column_filter = ColumnsFilter(request.GET, queryset=Columns.objects.all())
    return render(request, 'main/column_list.html', {'filter' : column_filter})

def cementing_list(request):
    cementing_filter = CementingFilter(request.GET, queryset=Cementing.objects.all())
    return render(request, 'main/cementing_list.html', {'filter' : cementing_filter})
    

