from flask import Flask, request, redirect, render_template
import os
#import jinja2


#template_dir = os.path.join(os.path.dirname(__file__),'templates')
#jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader
#(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True


#creates route handeler for the login page that makes each placeholder element in the form, an empty string (before any data input)
@app.route('/')
def display_login_form():
    return render_template('signup.html')


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
         

    if len(password) < 3  or len(password) > 20: 
        password_error = 'Password Error: must be between 4-20 characters'
        

    if ' ' in password:
        password_error = 'Password Error: cannot contain spaces'
        

# Verify password validataion
    if verify =='':
        verify_error = 'Password Error: empty, must be between 4-20 characters'
        
    
    if len(verify) < 3  or len(verify) > 20: 
        verify_error = 'Password Error: must be between 4-20 characters'
        
    
    if verify != password:
        verify_error = 'Password Error: passwords do not match'
        
 
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
# Return template html pages for either 'welcome.html page' if form inputs are valid -or- login.html page showing all form input validation errors.
    if not username_error and not password_error and not verify_error and not email_error:
       #username = username  not needed as the variable 'username' value is held b/c either its global -or- this is still considered local area 
       return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error = username_error, password_error = password_error, 
        verify_error = verify_error, email_error = email_error, username = username, email = email)

@app.route('/welcome', methods = ['POST' and 'GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()