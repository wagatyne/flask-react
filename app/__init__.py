from flask import Flask, Markup, render_template, make_response, jsonify

# The create_app function initializes the application factory
def create_app():
    """ Create instance of Flask """
    app = Flask(__name__,instance_relative_config=True)

    @app.route("/<option>")
    def hello(option):
        data = {"id": 1, "first_name": "Arnold", "last_name": "Schwarzenegger"}
        if option == 'json':
            response = make_response(jsonify(data), 200)
            response.headers["Content-Type"] = "application/json"
            return response
        elif option == 'markup':
            return Markup('<h1>Hello Markup</h1>')
        elif option == 'template':
            return render_template('index.html')
        else:
            return "Hello World!"

    return app