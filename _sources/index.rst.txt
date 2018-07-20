.. Website documentation master file, created by
   sphinx-quickstart on Sun Jun 10 23:54:15 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

hello!
======

.. raw:: html

  <div class="container-fluid">
  <div class="row">
  <div class="col-md-6">

This site maintains some notes on different papers I have read and wrote. I use jupyter notebooks for executable examples.

For some papers, there are existing explications. However, the process of looking at these papers helps me understand them better, and might afford others another persepective.

This site is inspired by the formatting of seaborn and is built using sphinx.

.. raw:: html

  </div>
    <div class="col-md-3">
  <div class="panel panel-default">   
  <div class="panel-heading">
  <h3 class="panel-title">Posts</h3>
  </div>
  <div class="panel-body">

.. toctree::
   :maxdepth: 2
   :glob:

   posts/*

.. raw:: html

  </div>
  </div>
  </div>
  <div class="col-md-3">
  <div class="panel panel-default">   
  <div class="panel-heading">
  <h3 class="panel-title">Profile</h3>
  </div>
  <div class="panel-body">

.. toctree::
   :maxdepth: 2
   :glob:

   profile/research
   profile/publications
   profile/professional

.. raw:: html

  </div>
  </div>
  </div>
  </div>
  </div>