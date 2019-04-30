============================
format-task
============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt
.. _named placeholders: https://pyformat.info/#named_placeholders
.. _PyFormat: https://pyformat.info
.. _re.sub: https://docs.python.org/3/library/re.html#re.sub
.. _regular expression: https://en.wikipedia.org/wiki/Regular_expression

Step-functions task that applies the substitution, then formats
the results using a map of supplied arguments, and returns the results

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::

    {
        "Results": "my string {foobar} to format",
        "Arguments": {
            "foobar": 1,
        }
        "Pattern": "string",
        "Replacement": "gnirts",
        "SubstituteFirst": true
    }

    {
        "Results": [
            "my string {foobar} to format"
        ],
        "Arguments":{
            "foobar": 1,
        }
        "Pattern": "string",
        "Replacement": "gnirts",
        "SubstituteFirst": true
    }

    {
        "Results":{
            "myname": "my string {foobar} to format",
        }
        "Arguments":{
            "foobar": 1,
        }
        "Pattern": "string",
        "Replacement": "gnirts",
        "SubstituteFirst": true
    }

**Results**: Required
    A ``string``, ``map`` of ``string`` or ``list`` of ``string`` to
    format using *Arguments* and substitute using *Pattern* and *Replacement*.
    The response type will mirror the type used here. Formatting
    will be using the `PyFormat`_ `named placeholders`_. Substitution
    will be using the Python `re.sub`_ method.
**Arguments**: Optional
    A ``map`` of arguments to use to format the *Results*. Keys in
    this ``map`` should correspond to the format keys in *Results*.
    If absent an empty map will be used.
**Pattern**: Optional
    A `regular expression`_ used to identify replacements in
    *Results*. if absent a default of ``a^`` will be used.
**Replacement**: Optional
    The replacement string to use. If absent, then empty string will be used.
**SubstituteFirst**: Optional
    ``true`` if substitution should be applied before formatting, ``false``
    otherwise. If absent defaults to ``true``.

Response syntax
---------------

.. code::

    "my gnirts 1 to format"

    {
        "myname": "my gnirts 1 to format",
    }

    [
        "my gnirts 1 to format"
    ]

Lambda Package Location
-----------------------
https://s3.amazonaws.com/lambdalambdalambda-repo/quinovas/format-task/format-task-0.0.1.zip

License: `APL2`_
