$(function() {
    var timeout = null;

    // Remove qualquer ação ja existente e adiciona a do ajaxsearch
    $('#portal_ajaxsearch form input[type="text"]').unbind('keyup').unbind('keydown').unbind('keypress').bind('keyup', function(e) {
        var query = $(this).val();

        // Remove o timer anterior
        if(timeout != null) {
            clearTimeout(timeout);
        }

        // Verifica a quantidade minima para fazer a busca
        if(query.length < 3) {
            // Inicia o box dos resultados
            $('.ajaxsearch_result').html('');
            $('.ajaxsearch_result').hide();
            return true;
        }

        // Inicia o timer
        timeout = setTimeout("doAjaxRequest()", 1500);
    });

});

/*!
 * Remove os acentos
 */
var retira_acentos = function(palavra) {
    com_acento = 'áàãâäéèêëíìîïóòõôöúùûüçÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÖÔÚÙÛÜÇ';
    sem_acento = 'aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC';
    nova = '';
    for(i=0;i<palavra.length;i++) {
        if(com_acento.search(palavra.substr(i,1))>=0) {
            nova += sem_acento.substr(com_acento.search(palavra.substr(i,1)),1);
        }
        else {
            nova += palavra.substr(i,1);
        }
    }
    return nova;
};

/*!
 * Faz a requisição ajax
 */
var doAjaxRequest = function() {
    var query = $('#portal_ajaxsearch form input[type="text"]').val();
    
    // Faz a requisição do conteudo da busca
    $.ajax({
        url: './ajaxsearch',
        data: {'query': query},
        type: 'GET',
        dataType: 'json',
        success: function(data) {

            // Inicia o box dos resultados
            $('.ajaxsearch_result').html('');

            // Percorre os tipos
            $.each(data, function(index, grupo) {
               // Verifica se possui dados
                if(grupo.length > 0) {
                    var unique_name = retira_acentos(index.toLowerCase());
                    
                    // Cria o container do grupo
                    var out = '' +
                        '<div>' +
                            '<h3>' + index + '</h3>' + 
                            '<ul class="' + unique_name + '_result">' + 
                            '</ul>' + 
                        '</div>';
                    $('.ajaxsearch_result').append(out);

                    // Percorre os resultados do grupo
                    $.each(grupo, function(index, item) {
                        var li = '<li>' + 
                            '<a href="' + item.url + '">' + 
                            item.titulo + 
                            '</a>' + 
                            '</li>';

                        $('.' + unique_name + '_result').append(li);
                    });

                    // Adiciona o ver mais do grupo
                    var li = '<li class="ver-mais">' + 
                        '<a href="/url">' + 
                        'ver mais resultados para <span>' + query + '</span>' + 
                        '</a>' + 
                        '</li>';
                   $('.' + unique_name + '_result').append(li);
                }
            });

            // Adiciona o exibir todos os resultados
            var li = '<div class="ver-mais-geral">' + 
                '<a href="#">' + 
                'ver todos os resultados para <span>' + query + '</span>' + 
                '</a>' + 
                '</div>';
            $('.ajaxsearch_result').append(li);

            // Adiciona o evento para submeter o formulario
            $('.ver-mais-geral a').bind('click', function(e) {
                e.preventDefault();

                $('form[name="ajaxsearch_form"]').submit();
            });

            // Mostra o box do resultado
            $('.ajaxsearch_result').show();
        },
        error: function() {
            
        }
    });
}
