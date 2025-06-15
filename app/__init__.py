#import python project
from .config import DevelopmentConfig

def create_app():
    app = "Initialize Flask i.e. Flask(__name__, template_folder='blueprints/templates')"
    #app.config.from_object(DevelopmentConfig()) configure the app via object variables

    #from extensions import db
    #--initialize the db i.e., db.init_app(app)
    #--migrate, migrate.init_app(app,db)

    from .blueprints.models import all_models #loads all models

    #--initiate login_manager (if using Flask-Manager) i.e., 
    '''
    Example Code:
    login_manager.init_app(app) 
    from .config import LoginManagerConfig
    LoginManagerConfig.config_login(login_manager)
    '''
    

    from .blueprints import all_blueprints
    for blueprint, prefix in all_blueprints:
        #app.register_blueprint(blueprint=blueprint, url_prefix=prefix)
        pass

    return app
