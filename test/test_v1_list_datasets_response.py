# coding: utf-8

"""
    fixpoint/llmproxy/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v1_list_datasets_response import V1ListDatasetsResponse

class TestV1ListDatasetsResponse(unittest.TestCase):
    """V1ListDatasetsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ListDatasetsResponse:
        """Test V1ListDatasetsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ListDatasetsResponse`
        """
        model = V1ListDatasetsResponse()
        if include_optional:
            return V1ListDatasetsResponse(
                datasets = [
                    openapi_client.models.v1_dataset.v1Dataset(
                        name = '', 
                        display_name = '', 
                        description = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return V1ListDatasetsResponse(
        )
        """

    def testV1ListDatasetsResponse(self):
        """Test V1ListDatasetsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
