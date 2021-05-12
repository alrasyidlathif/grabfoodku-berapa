import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    # python main.py goodbye lathif --formal
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.secho(f"Bye {name}!", fg=typer.colors.BLUE)

if __name__ == "__main__":
    app()
