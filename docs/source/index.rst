Welcome to Supplier Api Documentation
=====================================

Suppliers
-----------

.. function:: GET /api/v2/stock

      Get supplier sku stock details

      Returns example.

      :statuscode 200: Successful request.
      :statuscode 400: Bad request.

      Example request::

             GET https://data-api-staging.aws.zanui.com.au/v1/stock
      
      Example response::

      .. sourcecode:: js

        [
            {
               "zanui_sku": "string",
               "supplier_sku": "string",
               "qty": 0,
               "name": "string",
               "zanui_name": "string"
            }
        ]
