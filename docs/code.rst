Documenting Code
================

Python Code
-----------

Sphinx started as a Python documentation tool and as a result, has
strong capabilities in this area.  In particular, it is capable of extracting 
Python "docstrings" and inserting them into your overall documentation collection as you 
dictate.

In the KWIVER project we use docstrings to document individual module, classes, members and functions.   To
include this text in our documentation, we need to make sure that Sphinx can "import" our modules without side effects. 
Primarily this means that there should be no executable code (beyond function, class and variable definitions) in your
modules.  If you want to make your module executable on the command line for convenience or testing purposes, use the 
following construct to guard that code:

.. code-block:: python

    if __name__ == "__main__":
        # executable code when your module is called directly on the command line goes here

You'll also need to make sure that Sphinx can find your modules by making sure their locations are on the Python path.  You can do this by editing :file:`conf.py`  in your :file:`docs` directory.  Since Sphinx's configuration file is 
an actual Python file, you can use ``sys.path`` to adjust the Python path.  Typically for KWIVER projects we
keep python code in the the :file:`python` directory and python based commands in the :file:`bin` directory, both of which
are peers of the :file:`docs` directory.  Given this, we can add the following lines to top of our :file:`conf.py` file:

.. code-block:: python

    import sys
    import os

    sys.path.insert(0,"../python")
    sys.path.insert(0,"../bin")


Sphinx runs with the :file:`docs` directory as its current working directory, so these relative paths work.
 
Module Documentation Example
----------------------------
   
To include a module's documentation you use Sphinx's  ``automodule`` command like this::

    .. automodule:: kwiver_doctest
       :members:

What follows is documentation found in the :file:`kwiver_doctest.py` module included with this repository.
 
.. automodule:: kwiver_doctest
   :members:

Command Documentation Example
-----------------------------

For the KWIVER project, we use the ``argparse`` module to parse our command line arguments.   Among other things, this allows
us to use the sphinx-argparse_ extension which will automatically document commands based on the help text included when the
parser is built.  In order to use it you'd invoke it like this::


    .. argparse::
       :ref: kwiver-doctest-command.cli_parser
       :prog: kwiver-doctest-command

Which results in output like this:

.. argparse::
   :ref: kwiver-doctest-command.cli_parser
   :prog: kwiver-doctest-command

In order for this to work, you command mus tbe on the Python path that you set up in :file:`conf.py` and there must be a symbol (either
a function call or a variable) at the root level of the module that Sphinx can use to access the ``argparse`` object so that it 
can introspect the help text.  If you use a function (like we have here with ``cli_parser()``) make sure that the function *only* creates the ``argparse`` object
becuase it will be exectued within the Sphinx process when the documentation is generated.

.. _sphinx-argparse: https://sphinx-argparse.readthedocs.org/en/latest/
