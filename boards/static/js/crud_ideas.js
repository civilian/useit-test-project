window.Boards = {};

window.Boards.createHtlmIdea = function (text, id){
    return '\n<tr><td>' + text + 
            '</td><td><a class="btn btn-danger right-down" href="#">Delete</a>' +
             '<a class="btn btn-success right-down" href="#">Edit</a></td></tr>' ;

}

window.Boards.updateIdeas = function (url) {
    $.get(url).done(function (response) {
        if (!response.ideas) {return;}
        var rows = '';
        for (var i=0; i<response.ideas.length; i++) {
            var idea = response.ideas[i];
            rows += window.Boards.createHtlmIdea(idea.text, idea.id)
        }
        $('#id_idea_table').html(rows);
    });
};

window.Boards.initialize = function (params){
    window.Boards.updateIdeas(params.boardApiUrl);

    const form = $('#id_idea_form');
    form.on('submit', function(event) {
      const value = form.find('input[name="text"]').val();
      form.find('input[name="text"]').val('');
      event.preventDefault();
      $.post(params.ideasApiUrl, {
        'board': params.boardId,
        'text': value,
        'accepted': params.acceptedIdea,
        'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
      }).done(function () {
        // $('.has-error').hide();
        window.Boards.updateIdeas(params.boardApiUrl);
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
