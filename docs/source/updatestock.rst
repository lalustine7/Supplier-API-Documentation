Update Stock
======================

.. function:: POST /api/v1/stock

      Update supplier sku stock details

      :header Content-Type: application/json
      :header Authorization: Bearer <token>
      :statuscode 200: Successful Operation
      :statuscode 401: Unauthorized Token
    
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
