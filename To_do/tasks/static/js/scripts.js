$(document).ready(function () {

    // ESTE VAR EU ESTOU APONTANDO PARA O END URL DO MEU PROJETO
    var baseURL = 'http://127.0.0.1:8000/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    // VAR QUE PEGA O VALOR DA VAR QUE ESTA NO HTML SETADO PARA A TAG DE SELECT COM NOME FILTER
    var filter = $('#filter');

    $(deleteBtn).on('click', function (e) {
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if (result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function () {
        searchForm.submit();
    });

    //DEFINICAO DO QUE ACONTECERÁ QUANDO OCORRER UMA MUDANÇA NA OPCAO DO HTML COM TAG NAME = FILTER
    // estou usando JQuery
    $(filter).change(function () {
        var filter = $(this).val();
        // Aqui estou enviando para view do django o endereço com o parametro
        // olhar para a view tasklist, ela que monta a lista de tarefas
        window.location.href = baseURL + '?filter=' + filter;
    });
});