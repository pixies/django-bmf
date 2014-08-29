#!/usr/bin/python
# ex:set fileencoding=utf-8:
# flake8: noqa

from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from ..testcase import BMFViewTestCase


class NotificationTests(BMFViewTestCase):

    def test_notification(self):
        """
        """
        r = self.client.get(reverse('djangobmf:notification'), {})
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('djangobmf:notification'), {'ct': 1})
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('djangobmf:notification'), {'filter': "all"})
        self.assertEqual(r.status_code, 200)

        r = self.client.get(reverse('djangobmf:notification'), {'ct': 1, 'filter': "all"})
        self.assertEqual(r.status_code, 200)
