# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fixpoint_openapi.models.v1_create_app_logs_response import V1CreateAppLogsResponse

class TestV1CreateAppLogsResponse(unittest.TestCase):
    """V1CreateAppLogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CreateAppLogsResponse:
        """Test V1CreateAppLogsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CreateAppLogsResponse`
        """
        model = V1CreateAppLogsResponse()
        if include_optional:
            return V1CreateAppLogsResponse(
                success = True
            )
        else:
            return V1CreateAppLogsResponse(
        )
        """

    def testV1CreateAppLogsResponse(self):
        """Test V1CreateAppLogsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
