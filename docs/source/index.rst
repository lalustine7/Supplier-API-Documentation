Welcome to Supplier Api Documentation
=====================================

Suppliers
-----------

.. function:: GET /api/v2/stock

      Get supplier sku stock details
      :statuscode 200: Successful request
      
      Example request::

             GET https://data-api-staging.aws.zanui.com.au/v1/stock
      
      Example response::
        
        [
            {
              "zanui_sku": "string",
              "supplier_sku": "string",
              "qty": 0,
              "name": "string",
              "zanui_name": "string"
            }
        ]

      Status Codes:: 
        
        :statuscode 200: Successful request
