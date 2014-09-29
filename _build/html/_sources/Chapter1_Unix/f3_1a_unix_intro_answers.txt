
Exercise Unix-1 answers
~~~~~~~~~~~~~~~~~~~~~~~

If you get 'lost' or confused in any part of this exercise, don't panic,
just use these basic tools to make sure you know where you are on the
system (``pwd``) and/or change directory back to your home (``cd ~``)
and start again.

Your session for the exercise with ``cd``, ``ls`` and ``pwd`` should
have gone something like this:

Using ~ to mean 'home':
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    cd ~

.. parsed-literal::

    /Users/plewis


.. code:: python

    pwd



.. parsed-literal::

    u'/Users/plewis'



Now, let's make sure we understand *dot* ``.``:

.. code:: python

    cd .

.. parsed-literal::

    /Users/plewis


Get a listing (this will be different for different users!):

.. code:: python

    ls

.. parsed-literal::

    [34mDesktop[m[m/     [34mDropbox[m[m/     [34mMusic[m[m/       [34mSites[m[m/       [34mstuff[m[m/
    [34mDocuments[m[m/   [34mLibrary[m[m/     [34mPictures[m[m/    [34mgeogg122[m[m/
    [34mDownloads[m[m/   [34mMovies[m[m/      [34mPublic[m[m/      [34mpublic_html[m[m/


.. code:: python

    cd ~ucfajlg

.. parsed-literal::

    /Users/ucfajlg


.. code:: python

    pwd



.. parsed-literal::

    u'/Users/ucfajlg'



.. code:: python

    ls

.. parsed-literal::

    [34mDesktop[m[m/   [34mDownloads[m[m/ [34mMovies[m[m/    [34mPictures[m[m/  [34mSites[m[m/
    [34mDocuments[m[m/ [34mLibrary[m[m/   [34mMusic[m[m/     [34mPublic[m[m/


Or, get a listing without changing directory:

.. code:: python

    ls ~plewis

.. parsed-literal::

    [34mDesktop[m[m/     [34mDropbox[m[m/     [34mMusic[m[m/       [34mSites[m[m/       [34mstuff[m[m/
    [34mDocuments[m[m/   [34mLibrary[m[m/     [34mPictures[m[m/    [34mgeogg122[m[m/
    [34mDownloads[m[m/   [34mMovies[m[m/      [34mPublic[m[m/      [34mpublic_html[m[m/


.. code:: python

    ls ~ucfajlg

.. parsed-literal::

    [34mDesktop[m[m/   [34mDownloads[m[m/ [34mMovies[m[m/    [34mPictures[m[m/  [34mSites[m[m/
    [34mDocuments[m[m/ [34mLibrary[m[m/   [34mMusic[m[m/     [34mPublic[m[m/


.. code:: python

    ls ~plewis/Music

.. parsed-literal::

    [34miTunes[m[m/


Using absolute path names:
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    cd /Users/plewis

.. parsed-literal::

    /Users/plewis


.. code:: python

    pwd



.. parsed-literal::

    u'/Users/plewis'



.. code:: python

    cd /Users/ucfajlg

.. parsed-literal::

    /Users/ucfajlg


Not get a listing of the contents:

.. code:: python

    ls /Users/plewis

.. parsed-literal::

    [34mDesktop[m[m/     [34mDropbox[m[m/     [34mMusic[m[m/       [34mSites[m[m/       [34mstuff[m[m/
    [34mDocuments[m[m/   [34mLibrary[m[m/     [34mPictures[m[m/    [34mgeogg122[m[m/
    [34mDownloads[m[m/   [34mMovies[m[m/      [34mPublic[m[m/      [34mpublic_html[m[m/


.. code:: python

    ls .

.. parsed-literal::

    [34mDesktop[m[m/   [34mDownloads[m[m/ [34mMovies[m[m/    [34mPictures[m[m/  [34mSites[m[m/
    [34mDocuments[m[m/ [34mLibrary[m[m/   [34mMusic[m[m/     [34mPublic[m[m/


Using relative pathnames. First make sure you are in your home directory:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    cd ~

.. parsed-literal::

    /Users/plewis


.. code:: python

    pwd



.. parsed-literal::

    u'/Users/plewis'



.. code:: python

    ls

.. parsed-literal::

    [34mDesktop[m[m/     [34mDropbox[m[m/     [34mMusic[m[m/       [34mSites[m[m/       [34mstuff[m[m/
    [34mDocuments[m[m/   [34mLibrary[m[m/     [34mPictures[m[m/    [34mgeogg122[m[m/
    [34mDownloads[m[m/   [34mMovies[m[m/      [34mPublic[m[m/      [34mpublic_html[m[m/


Now we will move relative to this:

.. code:: python

    cd ../ucfajlg

.. parsed-literal::

    /Users/ucfajlg


.. code:: python

    pwd



.. parsed-literal::

    u'/Users/ucfajlg'



.. code:: python

    ls

.. parsed-literal::

    [34mDesktop[m[m/   [34mDownloads[m[m/ [34mMovies[m[m/    [34mPictures[m[m/  [34mSites[m[m/
    [34mDocuments[m[m/ [34mLibrary[m[m/   [34mMusic[m[m/     [34mPublic[m[m/


.. code:: python

    ls ../ucfajlg

.. parsed-literal::

    [34mDesktop[m[m/   [34mDownloads[m[m/ [34mMovies[m[m/    [34mPictures[m[m/  [34mSites[m[m/
    [34mDocuments[m[m/ [34mLibrary[m[m/   [34mMusic[m[m/     [34mPublic[m[m/


.. code:: python

    cd ../plewis

.. parsed-literal::

    /Users/plewis


.. code:: python

    pwd



.. parsed-literal::

    u'/Users/plewis'


