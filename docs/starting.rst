Getting Started
===============

We have adopted Sphinx_ as the documentation engine for the KWIVER_
project.  Sphinx's focus on making *writing* documentation as easy
as possible while still providing excellent support for *generating*
documentation was espeially attractive.   This project serves as
an example Sphinx documented project and contains meta-documentation
about how the documentation process for KWIVER projects works.


Environment
-----------

Sphinx is a Python_ based tool and requires a number of Python modules in
addition to the Sphinx module itself.  At the KWIVER project, we frequently use
the Miniconda_ project from Continuum_ to provide out Python environment.
This provides a cross-platorm (Windows, Linux and Mac OS X), consistent
environment that's easy to install and maintain.

Miniconda provides it's own package manager, conda_ which can be used to
install most of the packages required for Sphinx based documnetation.  Conda
also supports the creation of Python "sandboxes" or virtual environments.  We
typically keep a "Sphinx" environment available, which can be created this way::

    conda create -n Sphinx sphinx sphinx_rtd_theme

Which will install the Sphinx tools (and all of Sphinx's dependencies) and the
Sphinx ReadTheDocs_ theme (which is the current default KWIVER theme)

Once you've created the Sphinx environment you activate it this way::

    source activate Sphinx

Quickstart
----------

Sphinx provides a command that initializes a project with a Sphinx
configuration file and stubs for some key documentation files called
``sphinx-quickstart``.  We create a :file:`docs` directory within our KWIVER
projects that contains these files.   While you're at it, you may wish to create a 
:file:`.gitignore` file containing ``docs/_build`` (at least) to avoid seeing the projects'
documentation build artificats in your ``git status`` results.

When you run `sphinx-quickstart` in the
:file:`docs` directory it will ask a you a series of questions.  In general
you'll have to decide on the answers to may of these based on the needs of your 
project but there are some key settings that are useful:

- We use :file:`.rst` as the source file suffix
- We turn on the EPub builder
- We turn on `autodoc`, `intersphinx` and `viewcode`
- We use :file:`index.rst` as our anchor document

Once you've run ``sphinx-quickstart``,  you can edit :file:`index.rst` to begin 
writing your documentation.  We find the Sphinx `reStructuredText Primer`_ to be a useful introduction to the 
documentation format used by Sphinx.

For KWIVER projects, we typically edit the :file:`conf.py` file to change ``html_theme`` to ``sphinx_rtd_theme``.

Preview
-------

Since reStructuredText is a mark up syntax that you work with in a text editor, you will need some 
means to see what your rendered documentation will look like.  While you can simply run ``make html`` in your :file:`docs` directory and open 
the resulting :file:`.html` file, this can become somewhat tedious.  If you install the ``livereload`` module in your Sphinx environment (``pip install livereload`` should do the trick) you can use the following Python script:

.. code-block:: python

    from livereload import Server, shell
    server = Server()
    server.watch("*.rst", shell('make html', cwd='.'))   #'*
    server.serve(root='_build/html')

Save this in your :file:`docs` directory as :file:`sphinx_server.py` and run it with this command::

    python sphinx_server.py

Then, you can browse to ``http://localhost:5500/`` to see your
rendered documentation.  The ``livereload`` module will notice
whenever you save a new version of one of your :file:`*.rst` files and will re-run sphinx to provide an updated view of you rendered documentation.

.. _Sphinx: http://sphinx-doc.org/
.. _KWIVER: http://kwiver.org/
.. _Python: http://python.org
.. _Miniconda: http://conda.pydata.org/miniconda.html
.. _Continuum: https://www.continuum.io/
.. _conda: http://conda.pydata.org/docs/
.. _ReadTheDocs: http://readthedocs.org
.. _reStructuredText Primer: http://sphinx-doc.org/rest.html

