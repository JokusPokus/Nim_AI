import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "3aaSG{7cu_p!rc'>"
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
    INITIAL_BOARD = [1, 3, 5, 7]

    def init_app(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
