# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential

from ._configuration import DevCenterConfiguration
from .operations import ProjectOperations
from .operations import PoolOperations
from .operations import ScheduleOperations
from .operations import DevBoxOperations
from .operations import EnvironmentsOperations
from .operations import ActionsOperations
from .operations import ArtifactsOperations
from .operations import CatalogItemOperations
from .operations import CatalogItemsOperations
from .operations import CatalogItemVersionsOperations
from .operations import EnvironmentTypeOperations
from . import models


class DevCenter(object):
    """The devcenter common definitions and endpoints.

    :ivar project: ProjectOperations operations
    :vartype project: dev_center.operations.ProjectOperations
    :ivar pool: PoolOperations operations
    :vartype pool: dev_center.operations.PoolOperations
    :ivar schedule: ScheduleOperations operations
    :vartype schedule: dev_center.operations.ScheduleOperations
    :ivar dev_box: DevBoxOperations operations
    :vartype dev_box: dev_center.operations.DevBoxOperations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: dev_center.operations.EnvironmentsOperations
    :ivar actions: ActionsOperations operations
    :vartype actions: dev_center.operations.ActionsOperations
    :ivar artifacts: ArtifactsOperations operations
    :vartype artifacts: dev_center.operations.ArtifactsOperations
    :ivar catalog_item: CatalogItemOperations operations
    :vartype catalog_item: dev_center.operations.CatalogItemOperations
    :ivar catalog_items: CatalogItemsOperations operations
    :vartype catalog_items: dev_center.operations.CatalogItemsOperations
    :ivar catalog_item_versions: CatalogItemVersionsOperations operations
    :vartype catalog_item_versions: dev_center.operations.CatalogItemVersionsOperations
    :ivar environment_type: EnvironmentTypeOperations operations
    :vartype environment_type: dev_center.operations.EnvironmentTypeOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = 'https://{devCenter}.{devCenterDnsSuffix}'
        self._config = DevCenterConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.project = ProjectOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pool = PoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.schedule = ScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dev_box = DevBoxOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.actions = ActionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.artifacts = ArtifactsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalog_item = CatalogItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalog_items = CatalogItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalog_item_versions = CatalogItemVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_type = EnvironmentTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DevCenter
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
