#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from djangobmf.views import ModuleCreateView
from djangobmf.views import ModuleUpdateView
from djangobmf.views import ModuleIndexView
from djangobmf.views import ModuleDetailView

from .forms import BMFQuotationUpdateForm
from .forms import BMFQuotationCreateForm

from .filters import QuotationFilter

import datetime


class QuotationCreateView(ModuleCreateView):
    form_class = BMFQuotationCreateForm

    def get_initial(self):
        self.initial.update({'date': datetime.datetime.now()})
        # LOOK ... this does not work in every case ?!?!
        # self.initial.update({'employee': self.request.djangobmf_employee.pk})
        return super(QuotationCreateView, self).get_initial()


class QuotationUpdateView(ModuleUpdateView):
    form_class = BMFQuotationUpdateForm


class QuotationDetailView(ModuleDetailView):
    form_class = BMFQuotationUpdateForm


class QuotationTableView(ModuleIndexView):
    filterset_class = QuotationFilter
