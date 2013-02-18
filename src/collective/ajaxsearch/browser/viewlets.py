# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets import common
from plone.app.layout.viewlets import content

from plone.app.i18n.locales.browser import selector

class AjaxSearchViewlet(common.SearchBoxViewlet):
    index = ViewPageTemplateFile('templates/searchbox.pt')