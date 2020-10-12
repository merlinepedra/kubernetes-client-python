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
from kubernetes.client.models.v1_service_account_token_projection import V1ServiceAccountTokenProjection  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ServiceAccountTokenProjection(unittest.TestCase):
    """V1ServiceAccountTokenProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ServiceAccountTokenProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_service_account_token_projection.V1ServiceAccountTokenProjection()  # noqa: E501
        if include_optional :
            return V1ServiceAccountTokenProjection(
                audience = '0', 
                expiration_seconds = 56, 
                path = '0'
            )
        else :
            return V1ServiceAccountTokenProjection(
                path = '0',
        )

    def testV1ServiceAccountTokenProjection(self):
        """Test V1ServiceAccountTokenProjection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
