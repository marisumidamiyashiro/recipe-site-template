function swap_form(){
    console.log("Test")
    let login_form = $('#login')
    let signup_form = $('#signup')
    let switch_button = $('#switch')

    console.log(switch_button.text())
    if(switch_button.text() == "Sign Up"){
        login_form.hide()
        signup_form.show()
        switch_button.html("Login")
    }
    else{
        login_form.show()
        signup_form.hide()
        switch_button.html("Sign Up")
    }

}