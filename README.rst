============================
format-task
============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

Step-functions task that formats a map using a supplied arguments map, and returns the results

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::

    {
        "Results":{
            "myname": "my string {foobar} to format",
        }
        "Arguments":{
            "foobar": 1,
        }
    }

Response syntax
---------------

.. code::

    {
        "myname": "my string 1 to format",
    }

Lambda Package Location
-----------------------
https://s3.amazonaws.com/lambdalambdalambda-repo/quinovas/format-task/format-task-0.0.1.zip

License: `APL2`_
