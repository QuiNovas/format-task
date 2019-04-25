============================
format-task
============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

Step-functions task that formats a map using a supplied arguments
map, and returns the results

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::

    {
        "Results": "my string {foobar} to format",
        "Arguments":{
            "foobar": 1,
        }
    }

    {
        "Results": [
            "my string {foobar} to format"
        ],
        "Arguments":{
            "foobar": 1,
        }
    }

    {
        "Results":{
            "myname": "my string {foobar} to format",
        }
        "Arguments":{
            "foobar": 1,
        }
    }

**Results**:
    A ``string``, ``map`` of ``string`` or ``list`` of ``string`` to
    format using *Arguments*. The response type will mirror the type
    used here. Formatting will be using the PyFormat named method.
**Arguments**:
    A ``map`` of arguments to use to format the *Results*. Keys in
    this ``map`` should correspond to the format keys in *Results*.

Response syntax
---------------

.. code::

    "my string 1 to format"

    {
        "myname": "my string 1 to format",
    }

    [
        "my string 1 to format"
    ]

Lambda Package Location
-----------------------
https://s3.amazonaws.com/lambdalambdalambda-repo/quinovas/format-task/format-task-0.0.1.zip

License: `APL2`_
