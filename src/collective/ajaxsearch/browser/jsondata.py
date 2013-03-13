# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility, queryUtility
from collective.ajaxsearch.interfaces.interfaces import IAjaxsearchSettings
from plone.registry.interfaces import IRegistry
import json

types = {
    'Crianças e Adolecentes' : 'Crianças e Adolescentes',
    'Pessoas com Deficiência' : 'Pessoa com Deficiência',
    'Pessoa Idosa' : 'Pessoa Idosa',
    'LGBT' : 'LGBT',
    'Adoção e Sequestro Internacional' : 'Adoção e Sequestro Internacional',
    'Atuação Internacional' : 'Atuação Internacional',
    'Mortos e Desaparecidos Políticos' : 'Mortos e Desaparecidos Políticos',
    'Combates às Violações' : 'Combates às Violações',
    'Combate ao Trabalho Escravo' : 'Combate ao Trabalho Escravo',
    'Direito Para Todos' : 'Direitos para Todos'
}

class AjaxSearchView(BrowserView):
    """
    class to create json search result
    """
    template = ViewPageTemplateFile('templates/searchresult.pt')

    def __call__(self):
        """
        Método que renderiza o resultado
        """
        search = {}
        output = {}

        # remove livesearch product
        livesearch = getToolByName(self.context, 'portal_javascripts')
        livesearch.getResource('livesearch.js').setEnabled(False)
        livesearch.cookResources()

        # Monta a query da busca
        query = self.request['query']

        # Executa a busca
        search['subject'] = [types[k] for k in types]
        search['sort_on'] = 'sortable_title'
        search['sort_order'] = 'ascending'
        search['review_state'] = 'published'

        # Faz a busca do conteudo
        ct = self.context.portal_catalog
        rs = ct(search)

        # Percorre os tipos para buscar
        for current_type in types:
            itens = [] 
            total_group = 0

            # Percorre os registros do catalog
            for brain in rs:

                # Verifica se está na mesma tag
                if types[current_type] in brain.Subject:

                    # Verifica se tem texto buscado
                    if brain.Title.lower().find(query.lower()) >= 0:

                        # Adiciona o registro à lista de resultados
                        itens.append({'url':brain.getPath(), 'titulo':brain.Title, 'subject':types[current_type]});

                        # Soma a quantidade total
                        total_group += 1

                        # Verifica se ja possui 3 resultados
                        if total_group == 3:
                            break

            # Adiciona a lista de resultados ao output
            output[current_type] = itens

        # Coloca os limites


        # Retorna o resultado em json
        return json.dumps(output)