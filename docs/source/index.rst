Welcome to Supplier Api Documentation
=====================================

Suppliers
+++++++++

.. http:get:: /api/v2/stock

      Get supplier sku stock details

      **Example request**:

      .. prompt:: bash $

             curl -H "Authorization: Token <token>" https://data-api-staging.aws.zanui.com.au/v1/stock
      
      **Example response**:

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
