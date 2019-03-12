window.Boards = {};

window.Boards.createHtlmIdea = function (text, id, homeUrl){
    const deleteUrl = homeUrl + 'ideas/delete/' + id;
    const editUrl =  homeUrl + 'boards/crud_user_ideas/' + id;
    return '\n<tr><td>' + text + 
            '</td><td><a class="btn btn-danger right-down" href="'+ deleteUrl + '">Delete</a>' +
             '<a class="btn btn-success right-down" href="'+ editUrl +'">Edit</a></td></tr>' ;

}

window.Boards.updateIdeas = function (boardApiUrl, homeUrl) {
    $.get(boardApiUrl).done(function (response) {
        if (!response.ideas) {return;}
        var rows = '';
        for (var i=0; i<response.ideas.length; i++) {
            var idea = response.ideas[i];
            rows += window.Boards.createHtlmIdea(idea.text, idea.id, homeUrl)
        }
        $('#id_idea_table').html(rows);
    });
};

window.Boards.initialize = function (params){
    window.Boards.updateIdeas(params.boardApiUrl, params.homeUrl);

    const form = $('#id_idea_form');
    form.on('submit', function(event) {
      const text = form.find('input[name="text"]').val();
      form.find('input[name="text"]').val('');
      event.preventDefault();
      $.post(params.ideasApiUrl, {
        'board': params.boardId,
        'text': text,
        'accepted': params.acceptedIdea,
        'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
      }).done(function () {
        // $('.has-error').hide();
        window.Boards.updateIdeas(params.boardApiUrl, params.homeUrl);
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
