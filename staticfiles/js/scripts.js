(function ($) {
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", window.csrftoken);
            }
        }
    });

    $('a.js-remove-photo').click(function () {
        var $el = $(this),
            url = $el.attr('href');

        $.post(url)
            .done(function () {
                $el.remove();
            })
            .fail(function () {
                alert("Can't delete photo");
            });

        return false;
    });

}($))
