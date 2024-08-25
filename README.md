Generate list for [Top Python Packages](https://pythontest.com/top-pytest-plugins).

This is a fork of: https://github.com/okken/top-pytest-plugins

This script is currently run locally.

Requires uv and then it will install httpx, rich, and typer for you.

## To run:

```bash
$ uv run top_python_packages.py
```

You may optionally add a package name to the command line:

```bash
$ uv run top_python_packages.py django
```

## This script was refactored using Claude 3.5 Sonnet

For full transparency, here are the prompts I used to refactor this script:

```plaintext
## Prompt:
Please update this script to use a rich table.

## Prompt:
Please update the table styles to be ascii so I can copy and paste it into a markdown doc

## Prompt:
Please remove the description column

## Prompt:
Please change all PyTest and pytest references to Django and django

## Prompt:
Please add back `if 'django' in project.lower() and 'django' != project.lower():`

## Prompt:
please remove the \*# Export to markdown section. I can just pipe the output \*

## Prompt:
Please add the typer library.

## Prompt:
Please remove days and limit

## Prompt:
Please refactor the script to allow me to pass the package name instead of django. You can default to django though.

This way I can pass pytest or flask or other projects.

## Prompt:
Please change the default Table box type to MARKDOWN
```
