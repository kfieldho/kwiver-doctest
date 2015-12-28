"""
``kwiver_doctest`` Module
+++++++++++++++++++++++++

The module level documentation can contain reStructuredText in it just like the ``.rst`` files that make up
a documenation collection.
"""

def sample_function(foo):
   """This is sample function documentation

    :param foo: A sample parameter
    :type foo: string
    :returns: True on success, or False on failure
    :rtype: bool
    :raises: AttributeError, KeyError


    Function documentation has special tags.  Click on the "source" link associated with this 
    function to see how this function was documented.   See the Sphinx `info field`_ documentation 
    for further details:

    .. _`info field`: http://sphinx-doc.org/domains.html#signatures
    """
