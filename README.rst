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

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Court of Auditors`: https://www.tcesc.tc.br/
.. _`Memo. DAE n° 020/2021`: https://www.tcesc.tc.br/sites/default/files/2021-06/Metodologia%20Estima%C3%A7%C3%A3o%20Populacional.pdf
