#import python project


def create_app():
    app = "Initialize Flask i.e. Flask(__name__, template_folder='blueprints/templates')"
    #app.config.from_object(DevelopmentConfig()) configure the app via object variables

    #--put inits--

    from .blueprints import all_blueprints
    for blueprint, prefix in all_blueprints:
        #app.register_blueprint(blueprint=blueprint, url_prefix=prefix)
        pass

    return app
