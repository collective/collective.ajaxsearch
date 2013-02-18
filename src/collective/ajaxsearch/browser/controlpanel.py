# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel

from collective.ajaxsearch.interfaces.interfaces import IAjaxsearchSettings
from collective.ajaxsearch.interfaces.interfaces import IAjaxsearchGroup

import zope.interface
from z3c.form.object import registerFactoryAdapter


class AjaxsearchSettingsEditForm(controlpanel.RegistryEditForm):
    """
    edit form for settings
    """
    schema = IAjaxsearchSettings
    label = u"Ajaxsearch settings"
    description = u""""""

    def updateFields(self):
        super(AjaxsearchSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(AjaxsearchSettingsEditForm, self).updateWidgets()


class AjaxsearchSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """
    control panel for settings
    """
    form = AjaxsearchSettingsEditForm


class AjaxsearchGroup(object):
    """
    group of config
    """
    zope.interface.implements(IAjaxsearchGroup)

registerFactoryAdapter(IAjaxsearchGroup, AjaxsearchGroup)
