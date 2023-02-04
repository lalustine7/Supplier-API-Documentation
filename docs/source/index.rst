Welcome to Supplier Api Documentation
=====================================

Suppliers
-----------

.. function:: GET /api/v2/stock

      Get supplier sku stock details
    
      Example request::

             GET https://data-api-staging.aws.zanui.com.au/v1/stock
      
      Example Successful response::
        
        [
            {
              "zanui_sku": "string",
              "supplier_sku": "string",
              "qty": 0,
              "name": "string",
              "zanui_name": "string"
            }
        ]
      
      Example Unsuccessful response::
        
        {
          "error": "string"
        }

      Status Codes:: 
        
        200: Successful request
        401: Unauthorized Token
