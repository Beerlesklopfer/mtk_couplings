from django.shortcuts import render
from django.views.generic import TemplateView

class CouplingsListView(TemplateView):
    template_name = 'couplings/index.html'

class CouplingDetailView(TemplateView):
    template_name = 'couplings/detail.html'
