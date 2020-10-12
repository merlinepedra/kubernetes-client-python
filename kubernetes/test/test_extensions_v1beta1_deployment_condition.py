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
from kubernetes.client.models.extensions_v1beta1_deployment_condition import ExtensionsV1beta1DeploymentCondition  # noqa: E501
from kubernetes.client.rest import ApiException

class TestExtensionsV1beta1DeploymentCondition(unittest.TestCase):
    """ExtensionsV1beta1DeploymentCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1DeploymentCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.extensions_v1beta1_deployment_condition.ExtensionsV1beta1DeploymentCondition()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1DeploymentCondition(
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return ExtensionsV1beta1DeploymentCondition(
                status = '0',
                type = '0',
        )

    def testExtensionsV1beta1DeploymentCondition(self):
        """Test ExtensionsV1beta1DeploymentCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
