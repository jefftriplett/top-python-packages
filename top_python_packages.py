# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "rich",
#     "typer",
# ]
# ///
import json
import httpx
import typer
from rich.console import Console
from rich.table import Table
from rich.box import MARKDOWN

console = Console()

def get_related_rows(json_data, package_name):
    for row in json_data['rows']:
        project = row['project'].lower()
        if package_name in project and package_name != project:
            yield row

def fetch_data(url: str):
    r = httpx.get(url)
    r.raise_for_status()
    return json.loads(r.text)

def create_table(data, package_name):
    table = Table(title=f"Top {package_name.capitalize()} Related Packages (excluding {package_name} itself)", box=MARKDOWN)
    table.add_column("#", style="cyan", no_wrap=True)
    table.add_column("Package", style="magenta")
    table.add_column("Downloads", style="green", justify="right")

    for i, row in enumerate(get_related_rows(data, package_name), start=1):
        table.add_row(
            str(i),
            row['project'],
            f"{row['download_count']:,}"
        )

    return table

def main(
    package_name: str = typer.Argument("pytest", help="The package name to search for related packages")
):
    data_source = 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json'

    try:
        data = fetch_data(data_source)
    except httpx.HTTPStatusError as e:
        console.print(f"[bold red]Error fetching data: {e}[/bold red]")
        raise typer.Exit(code=1)

    console.print(f"Data last updated: {data['last_update']}")

    table = create_table(data, package_name.lower())
    console.print(table)

if __name__ == '__main__':
    typer.run(main)
