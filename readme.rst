.. -*- coding: utf-8 -*-

===
Vid
===

:Author: Alexandre de Verteuil
:Contact: claudelepoisson@gmail.com
:Date: 2014-05-26

What do?
--------

Transform XML using XSL stylesheet.

Why?
----

INF6450 "Information Management With XML" course at Téluq.

Usage
-----

::

    usage: xslt.py [-h] input output [stylesheet]

    positional arguments:
      input       Name of an XML file
      output      Name of an XML file (will be overwritten)
      stylesheet  Name of an XSLT file (default try finding xml-stylesheet
                  processing instruction, otherwise same as input but with .xsl
                  extension)

There are three ways to specify the XSLT stylesheet file name. They are tried in this order:

#. If given, the third positional argument;
#. If found, the href attribute of the xml-stylesheet processing instruction;
#. If it exists, the file with the same base name but with an ``.xsl`` extension.

Installing
~~~~~~~~~~

At this time, there is no package or even a setup.py script. Just
install the required lxml module and put xslt.py in your $PATH.

Rough areas
~~~~~~~~~~~

You will know something went wrong from the user unfriendly Traceback and error message.

Requirements
------------

* Python 3.x
* `lxml`_

.. _`lxml`: https://pypi.python.org/pypi/lxml/

Contributing
------------

Get the source
~~~~~~~~~~~~~~

::

    $ # mkproject is from virtualenvwrapper
    $ mkproject xslt
    (xslt)$ git clone https://github.com/adeverteuil/xslt.git .
    (xslt)$ # You can also clone your own fork on GitHub.
    (xslt)$ pip install -r requirements.txt

Pushing code
~~~~~~~~~~~~

I don't expect much activity. Send me an email, or a pull request. I also
take comments.

Contact information
-------------------

:website: http://alexandre.deverteuil.net/
:email: alexandre@deverteuil.net
:GitHub: https://github.com/adeverteuil/xslt

Copying
-------

Copyright © 2014  Alexandre de Verteuil

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program (see LICENSE.txt).  If not, see
<http://www.gnu.org/licenses/>.
