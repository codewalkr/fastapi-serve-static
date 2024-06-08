import uvicorn, pathlib
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from pydantic_settings import BaseSettings

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    ENABLE_TLS: bool = False
    CONF_MAIN_APP_HOST: str = "0.0.0.0"
    CONF_MAIN_APP_PORT: int = 8080
    CONF_DEBUG_LEVEL: str = "debug"                                
    CONF_SSL_KEYFILE: str = ""  
    CONF_SSL_CERTFILE: str = "" 


settings = Settings()

app = FastAPI(
    title=f"FastAPI Static Web Server",
    description=f"A simple single file Python FastAPI application for serving a static web site.",
    version="1.0.0",
    docs_url=None,
    redoc_url=None
)

def configure():
    configure_routing()


def configure_routing():
    app.mount('/', StaticFiles(directory="site", html=True), name="site")


if __name__ == '__main__' and settings.ENABLE_TLS == True:
    configure()
    uvicorn.run(app,
                host=settings.CONF_MAIN_APP_HOST,
                port=settings.CONF_MAIN_APP_PORT,
                log_level=settings.CONF_DEBUG_LEVEL,     
                ssl_keyfile=settings.CONF_SSL_KEYFILE,   
                ssl_certfile=settings.CONF_SSL_CERTFILE)
elif __name__ == '__main__' and settings.ENABLE_TLS == False:
    configure()
    uvicorn.run(app,
                host=settings.CONF_MAIN_APP_HOST,
                port=settings.CONF_MAIN_APP_PORT,
                log_level=settings.CONF_DEBUG_LEVEL)
else:
    configure()
