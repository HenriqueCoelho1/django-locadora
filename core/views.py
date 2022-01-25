from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView, TemplateView

from .models import Service, Employee, Position, Feature
from .forms import ContactForm


class IndexView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["services"] = Service.objects.order_by("?").all()
        context["employees"] = Employee.objects.order_by("?").all()
        context["features_one"] = Feature.objects.all()[:3]
        context["features_two"] = Feature.objects.all()[3:6]
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, "E-mail send with success")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Error in send this e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class TestView(TemplateView):
    template_name = "testing.html"
