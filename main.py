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
        <form method ="POST">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for "username">Username</label>
                        </td>
                        <td>
                            <input name ="username" value="" type = "text">
                            <span class='error'></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for "password"><Password</label>
                        </td>
                        <td>
                            <input name = "password" type = "password">
                            <span class = "error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "verify">Verify Password</label>
                        </td>
                        <td>
                            <input name = "verify" type ="password">
                            <span class = "error"></span>
                        </td>
                        <td>   
                            label for = "email">Email (Optional)</label>
                        </td>
                        <td>
                            <input name = "email" type = "text" value ="">
                            <span class="error"></span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit'>
        </form>
    </body>
</html>
"""


