# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.extensions_v1beta1_id_range import ExtensionsV1beta1IDRange  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1IDRange(unittest.TestCase):
    """ExtensionsV1beta1IDRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1IDRange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_id_range.ExtensionsV1beta1IDRange()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1IDRange(
                max = 56, 
                min = 56
            )
        else :
            return ExtensionsV1beta1IDRange(
                max = 56,
                min = 56,
        )

    def testExtensionsV1beta1IDRange(self):
        """Test ExtensionsV1beta1IDRange"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
