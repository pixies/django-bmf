#!/usr/bin/python
# ex:set fileencoding=utf-8:

from __future__ import unicode_literals

from djangobmf.sites import site

from .models import Task
from .models import Goal

from .views import TaskIndexView
from .views import GoalCloneView
from .views import GoalIndexView
from .views import GoalDetailView

site.register(Task, **{
    'index': TaskIndexView,
})

site.register(Goal, **{
    'index': GoalIndexView,
    'clone': GoalCloneView,
    'detail': GoalDetailView,
})
