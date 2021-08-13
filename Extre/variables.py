import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from Extre.heroku import Var as Config
    from .var import Var
else:
    from local_config import Development as Config


Var = Config
