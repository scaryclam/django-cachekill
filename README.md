Django Cachekill
================

App to kill the django template cache without having to restart the django instance

What's the point?
-----------------

 - Sometimes a client may not want the production web server restarted or there may be restrictions on when this an happen
 - Perhaps there is restricted access to the server itself
 - The server hosts more than one site and another site has restrictions on how the server is restarted

In any case where the webserver can't be restarted, there may be a use for this application.

