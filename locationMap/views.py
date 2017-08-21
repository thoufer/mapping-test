from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.gis.geos import Point

import numpy as np
from UliEngineering.Math.Coordinates import BoundingBox

from .forms import ObservationAddForm, ObsAddForm
from .models import Observation

class ObservationCreateView(FormView):
    template_name = 'form.html'
    form_class = ObservationAddForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super(ObservationCreateView, self).form_valid(form)

class ObsAddView(FormView):
    template_name = 'form2.html'
    form_class = ObsAddForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super(ObsAddView, self).form_valid(form)


class LandingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """ get all observation points """
        queryset = Observation.objects.all()

        ''' Find bounding rectangle for all points '''
        qsLocations = np.array(queryset.values_list('location', flat= True))
        bbox = BoundingBox(qsLocations)

        return {'observations': queryset,
                'bbox': bbox}
