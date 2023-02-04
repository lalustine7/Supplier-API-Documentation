Get Stock
===================

.. http:get:: /api/v1/stock

      Get supplier sku stock details

      :header Content-Type: application/json
      :header Authorization: Bearer <token>
      :statuscode 200: Successful Operation
      :statuscode 401: Unauthorized Token


      .. tabs::

          .. tab:: Staging
    
              **Example request**:

                    GET https://data-api-staging.aws.zanui.com.au/v1/stock

          .. tab:: Production
    
              **Example request**:

                    GET https://data-api.aws.zanui.com.au/v1/stock
          
      
      **Example Successful response**:

      .. sourcecode:: json
        
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
        
        200: Successful Operation
        401: Unauthorized Token