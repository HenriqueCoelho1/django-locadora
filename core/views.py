from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Service, Employee, Position, Feature
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.order_by("?").all()
        context["employees"] = Employee.objects.order_by("?").all()
        context["features_one"] = Feature.objects.all()[:3]
        context["features_two"] = Feature.objects.all()[3:6]
        return context
