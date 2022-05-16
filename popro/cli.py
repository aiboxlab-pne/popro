"""Console script for popro."""
import os
import sys
from email.policy import default

import click

import popro


@click.command()
@click.option(
    "-ic",
    "--input_census",
    "path_census",
    type=click.STRING,
    help="Path to the census dataset in csv file. "
    + "Columns required: age, population, place, year",
)
@click.option(
    "-ib",
    "--input_birth",
    "path_births",
    type=click.STRING,
    help="Path to the births dataset in csv file. "
    + "Columns required: year, place, births",
)
@click.option(
    "-ip",
    "--input_population",
    "path_population",
    type=click.STRING,
    help="Path to the population dataset in csv file. "
    + "Columns required: year, place, population",
)
@click.option(
    "-yc",
    "--year_census",
    "year_census",
    type=click.INT,
    help="Year of the census dataset.",
)
@click.option(
    "-y", "--year", "year", type=click.INT, help="Year of projection."
)
@click.option(
    "-p", "--place", "place", type=click.INT, help="Projection place."
)
@click.option("-a", "--age", "age", type=click.INT, help="Projection age.")
@click.option(
    "-o",
    "--output",
    "output_path",
    type=click.STRING,
    default="",
    help="CSV file path of the projection report to be generated.",
)
@click.option(
    "-oe",
    "--outerr",
    "output_error",
    type=click.STRING,
    default="",
    help="CSV file path from the error report to be generated."
    + "Displays which combinations of the year and locality it was not "
    + "possible to project and the reason.",
)
@click.option(
    "-v",
    "--verbose",
    default=False,
    help="Show the algebraic expression of the calculus",
)
def main(
    path_census,
    path_births,
    path_population,
    year_census,
    year,
    place,
    age,
    output_path="",
    output_error="",
    verbose=False,
):
    """Console script for popro."""
    if path_census is None:
        click.echo("For help, type: popro --help")
        return

    engine = popro.Popro(
        path_census, path_births, path_population, year_census
    )

    if output_path != "":
        engine.project_all(output_path, output_error)
    else:
        population = engine.project(year, place, age, verbose)
        print(population)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
