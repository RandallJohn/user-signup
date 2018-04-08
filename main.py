from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True



form = """

<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {
                color:red; 
            }
        </style>   
    </head>    
    <body>
        <h1>Signup</h1>
        <form action = "/hello" method ="POST">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for "username">Username</label>
                        </td>
                        <td>
                            <input id = "username" name ="username" value="" type = "text"/>
                            <span class='error'></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for "password">Password</label>
                        </td>
                        <td>
                            <input id = "password" name = "password" type = "password"/>
                            <span class = "error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "verify">Verify Password</label>
                        </td>
                        <td>
                            <input id = "varify" name = "verify" type ="password"/>
                            <span class = "error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>   
                            <label for = "email">Email (Optional)</label>
                        </td>
                        <td>
                            <input id = "email" name = "email" type = "text" value =""/>
                            <span class="error"></span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit" value = "Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods = ['POST'])
def hello():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    
    
    return "<h1>hello, " + username + " at:" + email + "</h1>"


app.run()