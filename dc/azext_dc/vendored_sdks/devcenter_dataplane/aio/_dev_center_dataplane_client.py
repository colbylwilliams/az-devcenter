# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DevCenterDataplaneClientConfiguration
from .operations import ProjectOperations
from .operations import PoolOperations
from .operations import ScheduleOperations
from .operations import DevBoxOperations
from .operations import EnvironmentsOperations
from .operations import ArtifactsOperations
from .operations import CatalogItemOperations
from .operations import CatalogItemsOperations
from .operations import CatalogItemVersionsOperations
from .operations import EnvironmentTypeOperations
from .. import models


class DevCenterDataplaneClient(object):
    """DevBox API.

    :ivar project: ProjectOperations operations
    :vartype project: dev_center_dataplane_client.aio.operations.ProjectOperations
    :ivar pool: PoolOperations operations
    :vartype pool: dev_center_dataplane_client.aio.operations.PoolOperations
    :ivar schedule: ScheduleOperations operations
    :vartype schedule: dev_center_dataplane_client.aio.operations.ScheduleOperations
    :ivar dev_box: DevBoxOperations operations
    :vartype dev_box: dev_center_dataplane_client.aio.operations.DevBoxOperations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: dev_center_dataplane_client.aio.operations.EnvironmentsOperations
    :ivar artifacts: ArtifactsOperations operations
    :vartype artifacts: dev_center_dataplane_client.aio.operations.ArtifactsOperations
    :ivar catalog_item: CatalogItemOperations operations
    :vartype catalog_item: dev_center_dataplane_client.aio.operations.CatalogItemOperations
    :ivar catalog_items: CatalogItemsOperations operations
    :vartype catalog_items: dev_center_dataplane_client.aio.operations.CatalogItemsOperations
    :ivar catalog_item_versions: CatalogItemVersionsOperations operations
    :vartype catalog_item_versions: dev_center_dataplane_client.aio.operations.CatalogItemVersionsOperations
    :ivar environment_type: EnvironmentTypeOperations operations
    :vartype environment_type: dev_center_dataplane_client.aio.operations.EnvironmentTypeOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param tenant_id: The tenant to operate on.
    :type tenant_id: str
    :param dev_center: The DevCenter to operate on.
    :type dev_center: str
    :param dev_center_dns_suffix: The DNS suffix used as the base for all devcenter requests.
    :type dev_center_dns_suffix: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        tenant_id: str,
        dev_center: str,
        dev_center_dns_suffix: str = "devcenter.azure.com",
        **kwargs: Any
    ) -> None:
        base_url = 'https://{tenantId}-{devCenter}.{devCenterDnsSuffix}'
        self._config = DevCenterDataplaneClientConfiguration(credential, tenant_id, dev_center, dev_center_dns_suffix, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

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

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DevCenterDataplaneClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
