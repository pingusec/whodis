import typer
import ui_utils
from rich import print
from rich.console import Console

app = typer.Typer()
console = Console()

# Entry point into the application
@app.command()
def main():
    print("Whodis")
    

if __name__ == "__main__":
    app()