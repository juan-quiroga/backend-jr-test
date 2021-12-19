import click

import migrations


@click.group()
def entry_point():
    pass


@entry_point.command()
def initialize_db():
    migrations.run()


if __name__ == '__main__':
    entry_point()

