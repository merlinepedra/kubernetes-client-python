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
from kubernetes.client.models.extensions_v1beta1_runtime_class_strategy_options import ExtensionsV1beta1RuntimeClassStrategyOptions  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1RuntimeClassStrategyOptions(unittest.TestCase):
    """ExtensionsV1beta1RuntimeClassStrategyOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1RuntimeClassStrategyOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_runtime_class_strategy_options.ExtensionsV1beta1RuntimeClassStrategyOptions()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1RuntimeClassStrategyOptions(
                allowed_runtime_class_names = [
                    '0'
                    ], 
                default_runtime_class_name = '0'
            )
        else :
            return ExtensionsV1beta1RuntimeClassStrategyOptions(
                allowed_runtime_class_names = [
                    '0'
                    ],
        )

    def testExtensionsV1beta1RuntimeClassStrategyOptions(self):
        """Test ExtensionsV1beta1RuntimeClassStrategyOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
