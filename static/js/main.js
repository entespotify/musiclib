var hey = 'hiii';

console.log(hey);

$( document ).ready(function() {
    console.log( "ready!" );

    $('#login').click(function() {
        var username = $('#inputUsername').val();
        var password = $('#inputPassword').val();
        var users    = $('.users');
        $.ajax({
            url: '/api/accounts/login/token',
            type: 'post',
            data: {
                "username": username,
                "password": password
            },
            dataType: 'json',
            success: function (data) {
                console.info(data);
                console.info(data.token);
                $.ajax({
                    url: '/api/accounts/users',
                    type: 'get',
                    headers: {'Authorization': "Token "+data.token},
                    dataType: 'json',
                    success: function (data) {
                        console.log(data);
                        users.text(data);
                    }
                });
            }
        });
    });
});
