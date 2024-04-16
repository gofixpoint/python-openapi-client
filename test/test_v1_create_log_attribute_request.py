# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fixpoint_openapi.models.v1_create_log_attribute_request import V1CreateLogAttributeRequest

class TestV1CreateLogAttributeRequest(unittest.TestCase):
    """V1CreateLogAttributeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CreateLogAttributeRequest:
        """Test V1CreateLogAttributeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CreateLogAttributeRequest`
        """
        model = V1CreateLogAttributeRequest()
        if include_optional:
            return V1CreateLogAttributeRequest(
                log_attribute = fixpoint_openapi.models.v1_log_attribute.v1LogAttribute(
                    name = '', 
                    log_name = '', 
                    key = '', 
                    value = '', 
                    org_id = '', )
            )
        else:
            return V1CreateLogAttributeRequest(
        )
        """

    def testV1CreateLogAttributeRequest(self):
        """Test V1CreateLogAttributeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
