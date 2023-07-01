import typer
import click

from factories.config_factory import ConfigFactory
from factories.controller_factory import ControllerFactory
from controllers.login_controller import LoginController

app = typer.Typer()

@click.group()
def cli():
    load_app_config()
    pass

@click.command()
def login():
    controller: LoginController = ControllerFactory().create_object("login_controller")
    print(controller.login("", ""))
    click.echo("login")

@click.command()
def add_music_data():
    click.echo("Dropped the database")

@click.command()
def list_music_data():
    click.echo("Listing")

@click.command()
def delete_music_data():
    print("deleting")

@app.command()
def sub():
    pass

def load_app_config():
    loader = ConfigFactory().create_object('config_loader')
    loader.load_config()


typer_click_object = typer.main.get_command(app)
cli.add_command(login)
cli.add_command(add_music_data)
cli.add_command(list_music_data)
cli.add_command(delete_music_data)

if __name__ == "__main__":
    cli()