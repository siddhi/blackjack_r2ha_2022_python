blackjack-r2ha-2022-python
==========================

This is a Python reimplementation of Ted Young's `Blackjack kata <https://github.com/tedyoung/blackjack-r2ha-2022>`_ which is a part of the `"Refactoring to Hexagonal Architecture" <https://ted.dev/refactoring-to-hexagonal-architecture.html>`_ course

Requirements
------------

* You need to have Python 3.9+ installed on your machine
* You will also need git and any python code editor

Setup
-----

1. Install `hatch <https://hatch.pypa.io>`_: ``pip install hatch``
2. Download dependencies: From the project root, run ``hatch env create``
3. Run the unit tests: ``hatch run test``
4. To run the application: ``hatch run app``

Development
-----------

1. While coding you might want to use ``hatch run watch`` to run the tests in watch mode and automatically rerun tests when a file is saved
2. ``hatch run cov`` will run tests and give code coverage results
3. ``hatch run lint`` will lint the code using `ruff <https://github.com/charliermarsh/ruff>`_
4. ``hatch run format`` will reformat the code using `Black <https://github.com/psf/black>`_

License
-------

``blackjack-r2ha-2022-python`` is distributed under the terms of the `MIT <https://spdx.org/licenses/MIT.html>`_ license.
