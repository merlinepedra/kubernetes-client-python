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
from kubernetes.client.models.v1_azure_file_persistent_volume_source import V1AzureFilePersistentVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1AzureFilePersistentVolumeSource(unittest.TestCase):
    """V1AzureFilePersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1AzureFilePersistentVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_azure_file_persistent_volume_source.V1AzureFilePersistentVolumeSource()  # noqa: E501
        if include_optional :
            return V1AzureFilePersistentVolumeSource(
                read_only = True, 
                secret_name = '0', 
                secret_namespace = '0', 
                share_name = '0'
            )
        else :
            return V1AzureFilePersistentVolumeSource(
                secret_name = '0',
                share_name = '0',
        )

    def testV1AzureFilePersistentVolumeSource(self):
        """Test V1AzureFilePersistentVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
