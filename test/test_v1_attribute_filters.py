# coding: utf-8

"""
    fixpoint/v1/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fixpoint_openapi.models.v1_attribute_filters import V1AttributeFilters

class TestV1AttributeFilters(unittest.TestCase):
    """V1AttributeFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AttributeFilters:
        """Test V1AttributeFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AttributeFilters`
        """
        model = V1AttributeFilters()
        if include_optional:
            return V1AttributeFilters(
                keys = [
                    ''
                    ],
                values = [
                    ''
                    ]
            )
        else:
            return V1AttributeFilters(
        )
        """

    def testV1AttributeFilters(self):
        """Test V1AttributeFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
