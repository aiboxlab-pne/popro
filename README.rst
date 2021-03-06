=====
popro
=====


.. image:: https://img.shields.io/pypi/v/popro.svg
        :target: https://pypi.python.org/pypi/popro

.. image:: https://github.com/aiboxlab-pne/popro/actions/workflows/python-app.yml/badge.svg
        :target: https://github.com/aiboxlab-pne/popro/actions/workflows/python-app.yml

.. image:: https://readthedocs.org/projects/popro/badge/?version=latest
        :target: https://popro.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A population projection engine


* Free software: MIT license
* Documentation: https://popro.readthedocs.io.

Features
--------

* Calculates population projection segmented by age over the years
        * Methodology:
                * Presented by the Special Activities Board of the `Court of Auditors`_ of the State of Santa Catarina (Brazil), in the technical note `Memo. DAE n° 020/2021`_.
        * Overview:
                * Inputs:
                        * Specific year census dataset (place, age, population)
                        * Dataset of people born over the years (year, place, births)
                        * Projected population dataset not segmented by age over the years (year, place, population)
                * Output:
                        * Population projection segmented by age dataset (year, place, age, population)
                        * Errors report on combination of "place, age, year" unable to forecast (year, place, age, error_msg)

=====
Usage
=====

First let's generate Input CSV files to serve as a sample.

.. code-block:: python

   import csv

   def write_csv(file_path, list_data):
      with open(file_path, 'w', encoding='UTF8', newline='') as f:
         writer = csv.writer(f)
         for line in list_data:
               writer.writerow(line)

   data_birth = [['births', 'place', 'year'],
                 [102,'ny',2011],
                 [116,'ny',2012],
                 [94,'ny',2013],
                 [123,'ny',2014],
                 [156,'ny',2015]]

   data_census = [['age', 'population', 'place', 'year'],
                  [0, 100,  'ny', 2010],
                  [1, 110,  'ny', 2010],
                  [2, 105,  'ny', 2010],
                  [3, 102,  'ny', 2010]]

   data_population = [['population', 'place', 'year'],
                      [2010, 'ny', 2010],
                      [2100, 'ny', 2011],
                      [2050, 'ny', 2012],
                      [2040, 'ny', 2013],
                      [2090, 'ny', 2014],
                      [1950, 'ny', 2015]]

   write_csv(file_path='births.csv', list_data=data_birth)
   write_csv(file_path='census.csv', list_data=data_census)
   write_csv(file_path='population.csv', list_data=data_population)

Now let's import the lib Popro and generate our projection engine.

.. code-block:: python

   from popro import popro

   dict_input = {'path_census': 'census.csv', 'path_births': 'births.csv', 'path_population': 'population.csv', 'year_census': 2010}
   engine = popro.Popro(dict_input)

We are ready! Let's start by doing some punctual projections of year, age and place.

First we will try with an age and year whose birth of the group is prior to the census.

.. code-block:: python

   engine.project(year=2012, place='ny', age=3, verbose=True)


.. code-block:: text

   pop_ny_2010_age_1 * (pop_ny_2012 / pop_ny_2010)
   110 * (2050 / 2010)

   112.18905472636816


Now let's find out the projection for a group born after the census.

.. code-block:: python

   engine.project(year=2015, place='ny', age=4, verbose=True)


.. code-block:: text

   birth_ny_year_2011 * (pop_ny_2015 / pop_ny_2011)
   102 * (1950 / 2100)

   94.71428571428572

Finally we will generate a report with all possible combinations of year, age and place.

.. code-block:: python

   engine.project_all()


.. code-block:: text

   [{'year': 2011, 'place': 'ny', 'age': 0, 'quantity': 102.0},
    {'year': 2011, 'place': 'ny', 'age': 1, 'quantity': 104.4776119402985},
    {'year': 2011, 'place': 'ny', 'age': 2, 'quantity': 114.92537313432835},
    {'year': 2011, 'place': 'ny', 'age': 3, 'quantity': 109.70149253731343},
    {'year': 2012, 'place': 'ny', 'age': 0, 'quantity': 116.0},
    {'year': 2012, 'place': 'ny', 'age': 1, 'quantity': 99.57142857142857},
    {'year': 2012, 'place': 'ny', 'age': 2, 'quantity': 101.99004975124377},
    {'year': 2012, 'place': 'ny', 'age': 3, 'quantity': 112.18905472636816},
    {'year': 2013, 'place': 'ny', 'age': 0, 'quantity': 94.0},
    {'year': 2013, 'place': 'ny', 'age': 1, 'quantity': 115.43414634146342},
    {'year': 2013, 'place': 'ny', 'age': 2, 'quantity': 99.08571428571429},
    {'year': 2013, 'place': 'ny', 'age': 3, 'quantity': 101.49253731343283},
    {'year': 2014, 'place': 'ny', 'age': 0, 'quantity': 123.0},
    {'year': 2014, 'place': 'ny', 'age': 1, 'quantity': 96.30392156862744},
    {'year': 2014, 'place': 'ny', 'age': 2, 'quantity': 118.26341463414634},
    {'year': 2014, 'place': 'ny', 'age': 3, 'quantity': 101.51428571428572},
    {'year': 2015, 'place': 'ny', 'age': 0, 'quantity': 156.0},
    {'year': 2015, 'place': 'ny', 'age': 1, 'quantity': 114.76076555023923},
    {'year': 2015, 'place': 'ny', 'age': 2, 'quantity': 89.8529411764706},
    {'year': 2015, 'place': 'ny', 'age': 3, 'quantity': 110.34146341463415}]

Cool, but it would be better to export to a CSV, wouldn't it?

.. code-block:: python

   engine.project_all(output_report_projection_path='projection_report.csv')

Report generated!

CLI
-----

It is also possible to make projections via command line. Let's repeat the same projections:

.. code-block:: text

    $ popro -i path_census,census.csv -i path_births,births.csv -i path_population,population.csv -i year_census,2010 --year 2012 --place ny --age 3

.. code-block:: text

    112.18905472636816

.. code-block:: text

    $ popro -i path_census,census.csv -i path_births,births.csv -i path_population,population.csv -i year_census,2010 --year 2015 --place ny --age 4
.. code-block:: text

    94.71428571428572

.. code-block:: text

    $ popro -i path_census,census.csv -i path_births,births.csv -i path_population,population.csv -i year_census,2010 --output projection_report.csv

.. _`Court of Auditors`: https://www.tcesc.tc.br/
.. _`Memo. DAE n° 020/2021`: https://www.tcesc.tc.br/sites/default/files/2021-06/Metodologia%20Estima%C3%A7%C3%A3o%20Populacional.pdf
