from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True


@app.route('/')
def displaystuff():  # Function displays information for user to use before inputting
    html = ''
    html += '<html\n>'  # Open the HTML
    html += '<body\n>'  # Open the body
    html += '<form method="POST" action="form_input">\n'  # Open form
    # Ask the user for 1st inputted number
    html += 'Please input one number: <input type="text" name="num1" />\n'
    html += '<p>\n'
    # Ask the user for 2nd inputted number
    html += 'Please input another number: <input type="text" name="num2" />\n'
    html += '<p>\n'
    # Ask user for arithmetic operation: add, subtract, multiply, divide
    # If invalid input in box, by default, the operation done on numbers will be negative
    html += 'Please input a mathematical operation (+, -, *, /): <input type="text" name="opers" />\n'
    html += '<p>\n'
    # Create a submit button for the user to press after inputting
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'  # Close the form
    html += '</html>\n'  # Close the HTML
    html += '</body>\n'  # Close the body
    return html


@app.route('/form_input', methods=['POST'])
def takeinput():
    number1 = request.form['num1']  # User asked for 1st number to input - first as a string
    number2 = request.form['num2']  # User asked for 2nd number to input - first as a string
    operation = request.form['opers']  # User asked for an arithmetic operation - as a string
    if operation == "+":  # Converts the 2 numbers as float types and adds them together
        mathproblem = float(number1) + float(number2)
    elif operation == "-":  # Converts the 2 numbers as float types and subtracts them
        mathproblem = float(number1) - float(number2)
    elif operation == "/":  # Converts the 2 numbers as float types and divides them
        mathproblem = float(number1) / float(number2)
    else:
        # Converts the 2 numbers as float types and adds them together
        # If invalid input in any three boxes, by default, the program will return product of inputted numbers
        mathproblem = float(number1) * float(number2)
    html = ''
    html += '<html>\n'  # Open the HTML
    html += '<body>\n'  # Open the body
    # Returns to the user the operation done on the 2 inputted numbers
    html += 'Your calculation is: ' + str(mathproblem) + '\n'
    html += '</body>\n'  # Close the body
    html += '</html>\n'  # Close the HTML
    return html


if __name__ == '__main__':
    app.run()  # Runs the program

