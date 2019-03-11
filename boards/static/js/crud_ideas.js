window.Boards = {};


window.Boards.initialize = function (params){
    var form = $('#id_idea_form');
    form.on('submit', function(event) {
      event.preventDefault();
      console.log(form.find('input[name="text"]').val())
      $.post(params.ideasApiUrl, {
        'board': params.boardId,
        'text': form.find('input[name="text"]').val(),
        'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
      });
    });
};