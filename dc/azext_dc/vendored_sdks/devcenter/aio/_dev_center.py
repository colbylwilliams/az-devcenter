# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DevCenterConfiguration
from .operations import DevCentersOperations
from .operations import ProjectsOperations
from .operations import AttachedNetworksOperations
from .operations import GalleriesOperations
from .operations import ImagesOperations
from .operations import ImageVersionsOperations
from .operations import CatalogsOperations
from .operations import EnvironmentTypesOperations
from .operations import ProjectEnvironmentTypesOperations
from .operations import DevBoxDefinitionsOperations
from .operations import Operations
from .operations import OperationStatusesOperations
from .operations import UsagesOperations
from .operations import SkusOperations
from .operations import PoolsOperations
from .operations import SchedulesOperations
from .operations import NetworkConnectionsOperations
from .. import models


class DevCenter(object):
    """DevCenter Management API.

    :ivar dev_centers: DevCentersOperations operations
    :vartype dev_centers: dev_center.aio.operations.DevCentersOperations
    :ivar projects: ProjectsOperations operations
    :vartype projects: dev_center.aio.operations.ProjectsOperations
    :ivar attached_networks: AttachedNetworksOperations operations
    :vartype attached_networks: dev_center.aio.operations.AttachedNetworksOperations
    :ivar galleries: GalleriesOperations operations
    :vartype galleries: dev_center.aio.operations.GalleriesOperations
    :ivar images: ImagesOperations operations
    :vartype images: dev_center.aio.operations.ImagesOperations
    :ivar image_versions: ImageVersionsOperations operations
    :vartype image_versions: dev_center.aio.operations.ImageVersionsOperations
    :ivar catalogs: CatalogsOperations operations
    :vartype catalogs: dev_center.aio.operations.CatalogsOperations
    :ivar environment_types: EnvironmentTypesOperations operations
    :vartype environment_types: dev_center.aio.operations.EnvironmentTypesOperations
    :ivar project_environment_types: ProjectEnvironmentTypesOperations operations
    :vartype project_environment_types: dev_center.aio.operations.ProjectEnvironmentTypesOperations
    :ivar dev_box_definitions: DevBoxDefinitionsOperations operations
    :vartype dev_box_definitions: dev_center.aio.operations.DevBoxDefinitionsOperations
    :ivar operations: Operations operations
    :vartype operations: dev_center.aio.operations.Operations
    :ivar operation_statuses: OperationStatusesOperations operations
    :vartype operation_statuses: dev_center.aio.operations.OperationStatusesOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: dev_center.aio.operations.UsagesOperations
    :ivar skus: SkusOperations operations
    :vartype skus: dev_center.aio.operations.SkusOperations
    :ivar pools: PoolsOperations operations
    :vartype pools: dev_center.aio.operations.PoolsOperations
    :ivar schedules: SchedulesOperations operations
    :vartype schedules: dev_center.aio.operations.SchedulesOperations
    :ivar network_connections: NetworkConnectionsOperations operations
    :vartype network_connections: dev_center.aio.operations.NetworkConnectionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Unique identifier of the Azure subscription. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DevCenterConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.dev_centers = DevCentersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.projects = ProjectsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.attached_networks = AttachedNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.galleries = GalleriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.images = ImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.image_versions = ImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalogs = CatalogsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_types = EnvironmentTypesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.project_environment_types = ProjectEnvironmentTypesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dev_box_definitions = DevBoxDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_statuses = OperationStatusesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pools = PoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.schedules = SchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_connections = NetworkConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DevCenter":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
