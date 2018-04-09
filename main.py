from flask import Flask, request, redirect#, render_template
#import os
#import jinja2


#template_dir = os.path.join(os.path.dirname(__file__),'templates')
#jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader)
#(template_dir), autoescape =True

app = Flask(__name__)
app.config['DEBUG'] = True

login_form = """

<!DOCTYPE html>
<html>
    <head> <title> Sign Up </title>
        <style>
            .error {{
                color:red; 
            }}
        </style>   
    </head>    
    <body>
        <h1>SignUp</h1>
        <form action="/login" method ='POST'>
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
                            <input id = "verify" name = "verify" type ="password" />
                            </label>
                            <span class = "error">{verify_error}</span>
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
            <input type="submit"/>
        </form>
    </body>
</html>
"""
#creates route handeler for the login page that makes each placeholder element in the form, an empty string (before any data input)
@app.route('/')
def display_login_form():
    return login_form.format(username = '', username_error = '', password = '', password_error = '', verify = '', verify_error = '', email ='', email_error = '')


#create route handler for POSTING the form
@app.route('/login', methods = ['POST'])
def validate_login():
    
    #create variables to pull information out of form submitted through via flask request object
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    #create variables to contain error messages
    username_error = ''
    password_error =''
    verify_error = ''
    email_error = ''

# Verify username validation  
    if username =='':
        username_error = 'Username Error: empty, must be between 4-20 characters'
        username =''  

    if len(username) < 3 or len(username) > 20: 
        username_error = 'Username Error: must be between 4-20 characters'
        username =''

    if ' ' in username:
        username_error = 'Username Error: cannot contain spaces'
        username = ''

    
  # Verify password validations for: empty, lenght 4-20 char, has a space or password not matching
    
    if password == '':
        password_error = 'Password Error: empty, must be between 4-20 characters'
        password = ''  

    if len(password) < 3  or len(password) > 20: 
        password_error = 'Password Error: must be between 4-20 characters'
        password = ''

    if ' ' in password:
        password_error = 'Password Error: cannot contain spaces'
        password = ''

# Verify password validataion
    if verify =='':
        verify_error = 'Password Error: empty, must be between 4-20 characters'
        verify = ''
    
    if len(verify) < 3  or len(verify) > 20: 
        verify_error = 'Password Error: must be between 4-20 characters'
        verify = ''
    
    if verify != password:
        verify_error = 'Password Error: passwords do not match'
        verify = ''
 
# Verify Email  

    if email != '':
        if len(email) < 3 or len(email) > 20: 
            email_error = 'Email Error: must be between 4-20 characters'
            email =''

        if ' ' in email:
            email_error = 'Email Error: cannot contain spaces'
            email = ''

        if not email.count('@') == 1:
            email_error = 'Email Error: must be a valid email'
            email = ''
        if not email.count('.') == 1:
            email_error = 'Email Error: must be a valid email'
            email = ''


    if not username_error and not password_error and not verify_error and not email_error:
       return "success"
    else:
        return login_form.format(username_error = username_error, password_error = password_error, 
        verify_error=verify_error, email_error = email_error, username=username, email=email)


app.run()