from application import create_app
from application import routes

if __name__=='__main__':
    app = create_app("PROD")
    app.run(port=4000, debug=True,host="0.0.0.0") 
