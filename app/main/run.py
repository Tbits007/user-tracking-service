from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka
from faststream import FastStream
from faststream.kafka import KafkaBroker

from app.main.config import Config
from app.main.ioc.providers.action import ActionProvider
from app.main.ioc.providers.root import RootProvider
from app.presentation.controllers.handlers import actions

# $env:PYTHONPATH="C:\\PythonProjects\\FastAPIprojects\\tracking-service\\src"
# faststream run --factory app.main.run:create_production_app


def create_production_app() -> FastStream:
    config = Config()
    broker = KafkaBroker(config.kafka.uri())
    _app = create_app()
    container = make_async_container(
        RootProvider(),
        ActionProvider(),
        context={Config: config, KafkaBroker: broker},
    )
    setup_dishka(container, _app)
    return _app


def create_app() -> FastStream:
    _app = FastStream()
    set_brokers(_app)
    return _app


def set_brokers(_app: FastStream) -> None:
    _app.set_broker(actions)
