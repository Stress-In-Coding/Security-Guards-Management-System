from flask import Flask, render_template

def create_app():
    # Initialize Flask application
    app = Flask(__name__)
    
    # Define root route
    @app.route('/')
    def index():
        # Render the main dashboard template
        return render_template('index.html')
    
    return app
