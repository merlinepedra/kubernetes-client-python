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
from kubernetes.client.models.extensions_v1beta1_deployment_strategy import ExtensionsV1beta1DeploymentStrategy  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1DeploymentStrategy(unittest.TestCase):
    """ExtensionsV1beta1DeploymentStrategy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1DeploymentStrategy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_deployment_strategy.ExtensionsV1beta1DeploymentStrategy()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1DeploymentStrategy(
                rolling_update = kubernetes.client.models.extensions/v1beta1/rolling_update_deployment.extensions.v1beta1.RollingUpdateDeployment(
                    max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                type = '0'
            )
        else :
            return ExtensionsV1beta1DeploymentStrategy(
        )

    def testExtensionsV1beta1DeploymentStrategy(self):
        """Test ExtensionsV1beta1DeploymentStrategy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
