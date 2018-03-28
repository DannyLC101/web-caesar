from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config["DEBUG"] = True

page_header = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea{{
                    margin:10px;
                    width: 540px;
                    height:120px;
                }}
                p.error{
                    color:red;
                }
            </style>
        </head>
        <body>
           <form action='' method = "post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value='0'>
                <p class="error"></p>
            </div>
"""

page_footer="""
            <br>
            <input type="submit" value="SUBMIT"/>
           </form>  
        </body>
    </html>
"""

form = page_header + """

            <textarea type="text" name="text">{0}</textarea>
          
""" + page_footer

@app.route('/')
def index():
    return form  #.format(rot='', error='', text='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/', methods=["POST"])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']

    error = ''
    rot=int(rot)

    #if not is_integer(rot):
    #    error = 'Not a valid number'
    #    rot = ''
    #if not error:
        #success message
    final_str = rotate_string(text, rot)
        #return redirect('/?rot={0}'.format(final_str))
    #return form.format(text=final_str)
    display = page_header+ '<textarea type="text" name="text">'+ final_str +'</textarea>' +page_footer
    return display
    #else:
     #   return form.format(error=error)
app.run()
