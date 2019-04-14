============================
format-task
============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

descripition

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::

    {
        "results":{
            "myname": "my string {foobar} to format",
        }
        "arguments":{
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
