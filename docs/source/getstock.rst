Get Stock
===================

.. http:get:: /api/v1/stock

      Get supplier sku stock details

      **Example request**:

      .. sourcecode:: http
          
          GET /v1/stock HTTP/1.1
          Host: https://data-api-staging.aws.zanui.com.au
          Accept: application/json
      
      **Example response**:

      .. sourcecode:: http
        
          HTTP/1.1 200 OK
          Vary: Accept
          Content-Type: application/json

          [
              {
                "zanui_sku": "string",
                "supplier_sku": "string",
                "qty": 0,
                "name": "string",
                "zanui_name": "string"
              }
          ]
      
      :reqheader Accept: the response content type depends on
                          :mailheader:`Accept` header
      :reqheader Authorization: optional OAuth token to authenticate
      :resheader Content-Type: this depends on :mailheader:`Accept`
        header of request
      :statuscode 200: Successful Operation
      :statuscode 401: Unauthorized Token