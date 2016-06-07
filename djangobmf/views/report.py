#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

# from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView

# from djangobmf.models import Report
from djangobmf.permissions import ModuleViewPermission
from djangobmf.views.mixins import ModuleViewMixin

# from .mixins import ModuleViewPermissionMixin
# from .mixins import ModuleViewMixin


class ReportBaseView(ModuleViewMixin, DetailView):
    """
    render a report
    """
    permission_classes = [ModuleViewPermission]
    context_object_name = 'object'

    # the view is connected to an object
    has_object = False

    # what name should the file generated by this report have
    default_filename = "report"

    # defines how the file is send, valid are "inline" or "attachment" or falsy
    default_disposition = "inline"

    # adds a suffix to the reports template_name path
    report_template_name_suffix = None

    # define the view's verbose name
    verbose_name = _("Report")

    # specify a form_class which can add additional informations to the report
    # TODO: currently not working
    form_class = None

    def get(self, request, *args, **kwargs):
        return self.get_report(request=self.request)

    def get_filename(self):
        """
        returns the filename which is used for the generateted report.
        By default it returns the default_filename attribute.
        """
        return self.default_filename

    def get_disposition(self):
        """
        returns the default disposition
        """
        return self.default_disposition

    def report_template_name(self):
        model = self.get_bmfmodel()

        if self.has_object:
            grain = "detail"
        else:
            grain = "list"

        if self.report_template_name_suffix:
            return '%s/%s_bmfreport_%s_%s.html' % (
                model._meta.app_label,
                model._meta.model_name,
                grain,
                self.report_template_name_suffix,
            )
        else:
            return '%s/%s_bmfreport_%s.html' % (
                model._meta.app_label,
                model._meta.model_name,
                grain
            )

    def get_report(self, **kwargs):
        """
        generates a report and returns a HttpResponse instance.
        """
        if "template_name" not in kwargs:
            kwargs["template_name"] = self.report_template_name()

        suffix, mime, data, send = self.kwargs['renderer'].render(**kwargs)

        filename = '%s.%s' % (self.get_filename(), suffix)
        disposition = self.get_disposition()

        response = HttpResponse(data)
        response['Content-Type'] = mime
        response['Content-Length'] = len(data)

        if send and disposition:
            response['Content-Disposition'] = '%s; filename=%s' % (
                disposition,
                filename,
            )

        return response
