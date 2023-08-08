from flask import Blueprint

insert_command = Blueprint('insert', __name__)

@insert_command.cli.command("new")
def new():
 pass