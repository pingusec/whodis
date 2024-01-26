import typer
import ui_utils
from rich import print
from rich.console import Console

app = typer.Typer()
console = Console()

# Entry point into the application
@app.command()
def main():
    print(ui_utils.getMainMenu())
    user_choice = typer.prompt('> Please enter your choice')

    match user_choice:
        case '1':
            fakeLoginHandler()

# Method that handles fake login page option    
def fakeLoginHandler():
    ui_utils.clear(5) # Clearing prev menu
    
    print(ui_utils.getFakeLoginMenuOptions())
    user_choice = typer.prompt('> Please choose a login page')

    match user_choice:
        case '1':
            print('spool up test website')
if __name__ == "__main__":
    app()