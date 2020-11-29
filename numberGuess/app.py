from flask import Flask, render_template, request
import random 
import requests


app = Flask(__name__)

#generate target within defined range

@app.route("/")
def index():
    # target = random.randrange(1,101,1) 
    return render_template("index.html")


@app.route("/guess")

def game():
    # target = random.randrange(1,101,1) 

    value = request.args.get("value")
    if not value:
        return render_template("failure.html")
        
    try:
        value = int(value)
    except ValueError as e:
        return render_template("failure.html")

    if int(value) < 1 or int(value) > 100:
        return render_template("failure.html")

   
    # return render_template("guess.html", target = target)

    while True: 
        if value > target:
            message = "Too High"
            return render_template("guessHi.html", target = target)

        elif int(value) < target: 
            message = "Too Low"
            return render_template("guessLo.html", target = target)

        else: 
            return render_template("correct.html", value = value)
            break

    # def numberGuess():
    #     ''' asks for int value between defined range. Checks if value is int '''
    #     while True :
    #         value = input("Enter an integer between 1 and 100\n") 
    #         try:
    #             value = int(value)
    #             return str(value)
            
    #         except ValueError:
    #             return "Value must be an integer\n"

    # #get first guess
    # value = numberGuess()

    # #check if number is too low or too 
    # while True: 
        
    #     if value > target:
    #         value = numberGuess()
    #         return "Too High"

    #     elif int(value) < target: 
    #         value = numberGuess()
    #         return "Too Low"

    #     else: 
    #         return "Correct!"
    #         break


