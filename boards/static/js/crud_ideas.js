window.Boards = {};

window.Boards.createHtlmIdea = function (idea, homeUrl, currentUserBoard){
    const deleteUrl = homeUrl + 'ideas/delete/' + idea.id;
    const updateUrl =  homeUrl + 'ideas/update/' + idea.id;
    const acceptUrl =  homeUrl + 'ideas/confirm_accept/' + idea.id;
    let row = '\n<tr><td>' + idea.text + '</td>'
    if (currentUserBoard){
      row += '<td>'
      if(!idea.accepted){
        row += '<a class="btn btn-success right-down" href="'+ acceptUrl + '">Accept</a>';
      }
      row +='<a class="btn btn-danger right-down" href="'+ deleteUrl + '">Delete</a>' +
             '<a class="btn btn-success right-down" href="'+ updateUrl +'">Edit</a></td>' ;
    }
    row += '</tr>';
    return row;

}

window.Boards.updateIdeas = function (boardApiUrl, homeUrl, currentUserBoard) {
    $.get(boardApiUrl).done(function (response) {
        if (!response.ideas) {return;}
        var rows = '';
        for (var i=0; i<response.ideas.length; i++) {
            var idea = response.ideas[i];
            rows += window.Boards.createHtlmIdea(idea, homeUrl, currentUserBoard)
        }
        $('#id_idea_table').html(rows);
    });
};

window.Boards.initialize = function (params){
    window.Boards.updateIdeas(params.boardApiUrl, params.homeUrl, params.currentUserBoard);
    const form = $('#id_idea_form');
    form.on('submit', function(event) {
      const text = form.find('input[name="text"]').val();
      form.find('input[name="text"]').val('');
      event.preventDefault();
      $.post(params.ideasApiUrl, {
        'board': params.boardId,
        'text': text,
        'accepted': params.currentUserBoard,
        'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
      }).done(function () {
        // $('.has-error').hide();
        window.Boards.updateIdeas(params.boardApiUrl, params.homeUrl, params.currentUserBoard);
      }).fail(function (xhr) {
        $('.has-error').show();
        if (xhr.responseJSON) {
          $('.has-error .help-block').text(xhr.responseJSON.text || xhr.responseJSON.non_field_errors);
        } else {
          $('.has-error .help-block').text('Error talking to server. Please try again.');
        }
      });;
    });
};
