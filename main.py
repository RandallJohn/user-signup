from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True



login_form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{
                color:red; 
            }}
        </style>   
    </head>    
    <body>
        <h1>Signup</h1>
        <form method ='POST'>
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for = "username">Username
                        </td>
                        <td>
                            <input id = "username" name ="username" value='{username}' type = "text"/>
                            </label>
                            <span class='error'>{username_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "password">Password
                        </td>
                        <td>
                            <input id = "password" name = "password" type = "password"/>
                            </label>
                            <span class = "error">{password_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "verify">Verify Password
                        </td>
                        <td>
                            <input id = "verify" name = "verify" type ="password"/>
                            </label>
                            <span class = "error">{verify_password_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>   
                            <label for = "email">Email (Optional)
                        </td>
                        <td>
                            <input id = "email" name = "email" type = "text" value ="{email}"/>
                            </label>
                            <span class="error">{email_error}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit" value = "Submit Query" />
        </form>
    </body>
</html>
"""
#creates route handeler for the login page that makes each placeholder element in the form, an empty string (before any data input)
@app.route('/login')
def display_login_form():
    return login_form.format(username ='', username_error ='', password_error = '', verify_password_error = '', email ='', email_error = '')


@app.route('/login', methods = ['POST'])
def suc():
    return "success"
#def validate_login():
    
    #create variables to pull information out of form submitted through via flask request object
 #   username = request.form['username']
  #  password = request.form['password']
 #   verify_password = request.form['verify_password']
 #   email = request.form['email']

    #create variables to contain error messages
#    username_error = ''
#    password_error =''
#    verify_password_error = ''
#    email_error = ''
    
#   if username > 20 or username <3: 
#        username_error = 'Username Error: must be between 4-20 characters'
#        username =''


#   username_error = 'Username Error: and cannot contain spaces'
#    username = ''

#    password_error = 'Password Error: must be between 4-20 characters'
#    password= ''

#    password_error = 'Password Error: and cannot contain spaces'
#    password = ''

#    verify_password_error = 'Verify password Error: passwords did not match'


#    email_error = 'Email Error: must be a valid email name 4-20 characters'
#    email = ''
    
#    email_error = 'Email Error: with no spaces, contain an @ and period(.) ex. sample@domain.com'
#    email = ''


#    if not username_error and not password_error and not email_error:
#        return "success"
#    else:
#        return login_form.format(username_error = username_error, password_error = password_error, 
#        verify_password_error=verify_password_error, email_error = email_error, username=username, email=email)


app.run()