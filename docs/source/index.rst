Welcome to Supplier Api Documentation
=====================================

Get Supplier Stock
-------------------

.. function:: GET /api/v1/stock

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


Update Supplier Stock
----------------------

.. function:: POST /api/v1/stock

      Update supplier sku stock details

      :json param1: Description of first JSON parameter.
      :json param2: Description of second JSON parameter.
      :header Content-Type: application/json
      :statuscode 200: Successful request.
      :statuscode 400: Bad request.
    
      Example request::

             POST https://data-api-staging.aws.zanui.com.au/v1/stock

       [
          {
            "zanui_sku": "string",
            "soh": 0
          }
        ]  
      
      Example Successful response::
        
        {
          "status": "string",
          "updated": [
            {
              "sku": "string",
              "soh": 0
            }
          ],
          "invalid_skus": [
            {
              "sku": "string",
              "soh": 0
            }
          ]
        }
      
      Example Unsuccessful response::
        
        {
          "error": "string"
        }

      Status Codes:: 
        
        200: Successful request
        401: Unauthorized Token
