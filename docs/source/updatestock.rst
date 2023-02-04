Update Stock
======================

.. http:post:: /api/v1/stock

      Update supplier stock details

      **Example request**:

        .. tabs::

            .. tab:: Staging

                .. sourcecode:: http
                    
                    POST /v1/stock HTTP/1.1
                    Host: https://data-api-staging.aws.zanui.com.au
                    Accept: application/json
                    Content-Type: application/json

                    [
                      {
                        "zanui_sku": "string",
                        "soh": 0
                      }
                    ]

            .. tab:: Production

                .. sourcecode:: http
                    
                    POST /v1/stock HTTP/1.1
                    Host: https://data-api.aws.zanui.com.au
                    Accept: application/json
                    Content-Type: application/json

                    [
                      {
                        "zanui_sku": "string",
                        "soh": 0
                      }
                    ]


      
      **Example response**:

      .. sourcecode:: http
        
          HTTP/1.1 200 OK
          Vary: Accept
          Content-Type: application/json

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

     **Example unsuccessful response**:

      .. sourcecode:: http
        
          HTTP/1.1 401 OK
          Content-Type: application/json

          {
            "error": "string"
          }
      
      :reqheader Accept: the response content type depends on
                          :mailheader:`Accept` header
      :reqheader Authorization: optional OAuth token to authenticate
      :resheader Content-Type: this depends on :mailheader:`Accept`
        header of request
      :statuscode 200: Successful Operation
      :statuscode 401: Unauthorized Token