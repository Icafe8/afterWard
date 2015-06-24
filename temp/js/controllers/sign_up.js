/**
 * Created by jian on 15/6/10.
 */
$(function(){
    var formJo = $('#sign-up-form'),
        accountInputJo = formJo.find('#sign-up-email'),
        passwordInputJo = formJo.find('#sign-up-password');

    formJo.submit(function(e){
        //e.preventDefault();
        var data = {
            email: accountInputJo.val(),
            password: passwordInputJo.val()
        };
        $.ajax('/signup',{
            data: data,
            type: 'POST',
            success: function(response){
                console.log(response);
            }
        });
        return false;
    });
});