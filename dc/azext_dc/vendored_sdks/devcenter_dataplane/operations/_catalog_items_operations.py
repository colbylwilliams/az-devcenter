# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class CatalogItemsOperations(object):
    """CatalogItemsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~dev_center_dataplane_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        project_name,  # type: str
        catalog_item_id,  # type: str
        top=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CatalogItem"
        """Get a catalog item from a project.

        :param project_name: The DevCenter Project upon which to execute operations.
        :type project_name: str
        :param catalog_item_id: The unique id of the catalog item.
        :type catalog_item_id: str
        :param top: The maximum number of resources to return from the operation. Example: 'top=10'.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CatalogItem, or the result of cls(response)
        :rtype: ~dev_center_dataplane_client.models.CatalogItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CatalogItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2022-03-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'tenantId': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str', skip_quote=True),
            'devCenter': self._serialize.url("self._config.dev_center", self._config.dev_center, 'str', skip_quote=True),
            'devCenterDnsSuffix': self._serialize.url("self._config.dev_center_dns_suffix", self._config.dev_center_dns_suffix, 'str', skip_quote=True),
            'projectName': self._serialize.url("project_name", project_name, 'str', max_length=63, min_length=3, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9-]{2,62}$'),
            'catalogItemId': self._serialize.url("catalog_item_id", catalog_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if top is not None:
            query_parameters['top'] = self._serialize.query("top", top, 'int')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CatalogItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/projects/{projectName}/catalogItems/{catalogItemId}'}  # type: ignore
