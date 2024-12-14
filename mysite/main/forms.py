from django import forms
from .models import Well, Area, Columns, Cementing
import django_filters 
class Area_typeForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__' # [ 'id_area', 'area_name' ]
        labels = {
            'id_area' : 'ID участка',
            'area_name' : 'Название участка',
        }
        widgets = {
            'id_area': forms.TextInput(attrs={'class' : 'form-control'}),
            'area_name': forms.TextInput(attrs={'class' : 'form-control'}),
        }

class Well_typeForm(forms.ModelForm):
    class Meta:
        model = Well
        fields = '__all__' # [ 'id_area', 'area_name' ]
        labels = {
            'id_well' : 'ID скважины',
            'date_start' : 'Дата начала установка',
            'wellhead_coordinate_y' : 'Координата Y',
            'wellhead_coordinate_x' : 'Координата X',
            'altitude' : 'Альтитуда',
            'area' : 'Название участка',
        }
        widgets = {
            'id_well': forms.TextInput(attrs={'class' : 'form-control'}),
            'date_start': forms.TextInput(attrs={'class' : 'form-control'}),
            'wellhead_coordinate_y': forms.TextInput(attrs={'class' : 'form-control'}),
            'wellhead_coordinate_x': forms.TextInput(attrs={'class' : 'form-control'}),
            'altitude': forms.TextInput(attrs={'class' : 'form-control'}),
            'area': forms.TextInput(attrs={'class' : 'form-control'}),
        }

class Column_typeForm(forms.ModelForm):
    class Meta:
        model = Columns
        fields = '__all__' 
        labels = {
            'id_column' : 'ID колонны',
            'type_column' : 'Тип колонны',
            'date_installation' : 'Дата установки',
            'external_diameter' : 'Внутренний диаметр',

        }
        widgets = {
            'id_column': forms.TextInput(attrs={'class' : 'form-control'}),
            'type_column': forms.TextInput(attrs={'class' : 'form-control'}),
            'date_installation': forms.TextInput(attrs={'class' : 'form-control'}),
            'external_diameter': forms.TextInput(attrs={'class' : 'form-control'}),
        }

class Cementing_typeForm(forms.ModelForm):
    class Meta:
        model = Cementing
        fields = '__all__' 
        labels = {
            'id_cementing' : 'ID цементажа',
            'column_id' : 'ID колонны',
            'well_id' : 'ID колонны',
            'cementing_quality' : 'Качество',
            'cementing_start_date' : 'Дата начала',
            'cementing_end_date' : 'Дата окончания',

        }
        widgets = {
            'id_cementing': forms.TextInput(attrs={'class' : 'form-control'}),
            'column_id': forms.TextInput(attrs={'class' : 'form-control'}),
            'well_id': forms.TextInput(attrs={'class' : 'form-control'}),
            'cementing_quality': forms.TextInput(attrs={'class' : 'form-control'}),
            'cementing_start_date': forms.TextInput(attrs={'class' : 'form-control'}),
            'cementing_end_date': forms.TextInput(attrs={'class' : 'form-control'}),
        }

class AreaFilter(django_filters.FilterSet):
    class Meta:
        model = Area
        fields = ['id_area', 'area_name',]

class WellFilter(django_filters.FilterSet):
    class Meta:
        model = Well
        fields = ['id_well', 'date_start', 'wellhead_coordinate_y', 'wellhead_coordinate_x', 'altitude', 'area',]

class ColumnsFilter(django_filters.FilterSet):
    class Meta:
        model = Columns
        fields = ['id_column', 'type_column', 'date_installation', 'external_diameter',]

class CementingFilter(django_filters.FilterSet):
    class Meta:
        model = Cementing
        fields = ['id_cementing', 'column_id', 'well_id', 'cementing_quality', 'cementing_start_date', 'cementing_end_date', ]