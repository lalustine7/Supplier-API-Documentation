Testing Sphinx
===================

.. tip::
   This is useful for sharing access to an entire set of documentation for a user.
   You can embed these links in an internal wiki, for example,
   and all your employees will be able to browse the docs without a login.

.. prompt:: bash $

   curl -H "Authorization: Token 19okmz5k0i6yk17jp70jlnv91v" https://docs.example.com/en/latest/example.html


..  http:example:: curl wget httpie python-requests

    GET /Plone/front-page HTTP/1.1
    Host: localhost:8080
    Accept: application/json
    Authorization: Basic YWRtaW46YWRtaW4=