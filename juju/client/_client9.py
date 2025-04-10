# DO NOT CHANGE THIS FILE! This file is auto-generated by facade.py.
# Changes will be overwritten/lost when the file is regenerated.

from juju.client._definitions import *
from juju.client.facade import ReturnMapping, Type


class ModelManagerFacade(Type):
    name = "ModelManager"
    version = 9

    @ReturnMapping(ErrorResults)
    async def ChangeModelCredential(self, model_credentials=None):
        """ChangeModelCredential changes cloud credential reference for models.
        These new cloud credentials must already exist on the controller.

        model_credentials : typing.Sequence[~ChangeModelCredentialParams]
        Returns -> ErrorResults
        """
        if model_credentials is not None and not isinstance(
            model_credentials, (bytes, str, list)
        ):
            raise Exception(
                f"Expected model_credentials to be a Sequence, received: {type(model_credentials)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager",
            request="ChangeModelCredential",
            version=9,
            params=_params,
        )
        _params["model-credentials"] = model_credentials
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelInfo)
    async def CreateModel(
        self,
        cloud_tag=None,
        config=None,
        credential=None,
        name=None,
        owner_tag=None,
        region=None,
    ):
        """CreateModel creates a new model using the account and
        model config specified in the args.

        cloud_tag : str
        config : typing.Mapping[str, typing.Any]
        credential : str
        name : str
        owner_tag : str
        region : str
        Returns -> ModelInfo
        """
        if cloud_tag is not None and not isinstance(cloud_tag, (bytes, str)):
            raise Exception(
                f"Expected cloud_tag to be a str, received: {type(cloud_tag)}"
            )

        if config is not None and not isinstance(config, dict):
            raise Exception(
                f"Expected config to be a Mapping, received: {type(config)}"
            )

        if credential is not None and not isinstance(credential, (bytes, str)):
            raise Exception(
                f"Expected credential to be a str, received: {type(credential)}"
            )

        if name is not None and not isinstance(name, (bytes, str)):
            raise Exception(f"Expected name to be a str, received: {type(name)}")

        if owner_tag is not None and not isinstance(owner_tag, (bytes, str)):
            raise Exception(
                f"Expected owner_tag to be a str, received: {type(owner_tag)}"
            )

        if region is not None and not isinstance(region, (bytes, str)):
            raise Exception(f"Expected region to be a str, received: {type(region)}")

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="CreateModel", version=9, params=_params
        )
        _params["cloud-tag"] = cloud_tag
        _params["config"] = config
        _params["credential"] = credential
        _params["name"] = name
        _params["owner-tag"] = owner_tag
        _params["region"] = region
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ErrorResults)
    async def DestroyModels(self, models=None):
        """DestroyModels will try to destroy the specified models.
        If there is a block on destruction, this method will return an error.
        From ModelManager v7 onwards, DestroyModels gains 'force' and 'max-wait' parameters.

        models : typing.Sequence[~DestroyModelParams]
        Returns -> ErrorResults
        """
        if models is not None and not isinstance(models, (bytes, str, list)):
            raise Exception(
                f"Expected models to be a Sequence, received: {type(models)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="DestroyModels", version=9, params=_params
        )
        _params["models"] = models
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(StringResults)
    async def DumpModels(self, entities=None, simplified=None):
        """DumpModels will export the models into the database agnostic
        representation. The user needs to either be a controller admin, or have
        admin privileges on the model itself.

        entities : typing.Sequence[~Entity]
        simplified : bool
        Returns -> StringResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        if simplified is not None and not isinstance(simplified, bool):
            raise Exception(
                f"Expected simplified to be a bool, received: {type(simplified)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="ModelManager", request="DumpModels", version=9, params=_params)
        _params["entities"] = entities
        _params["simplified"] = simplified
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(MapResults)
    async def DumpModelsDB(self, entities=None):
        """DumpModelsDB will gather all documents from all model collections
        for the specified model. The map result contains a map of collection
        names to lists of documents represented as maps.

        entities : typing.Sequence[~Entity]
        Returns -> MapResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="DumpModelsDB", version=9, params=_params
        )
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelSummaryResults)
    async def ListModelSummaries(self, all_=None, user_tag=None):
        """ListModelSummaries returns models that the specified user
        has access to in the current server.  Controller admins (superuser)
        can list models for any user.  Other users
        can only ask about their own models.

        all_ : bool
        user_tag : str
        Returns -> ModelSummaryResults
        """
        if all_ is not None and not isinstance(all_, bool):
            raise Exception(f"Expected all_ to be a bool, received: {type(all_)}")

        if user_tag is not None and not isinstance(user_tag, (bytes, str)):
            raise Exception(
                f"Expected user_tag to be a str, received: {type(user_tag)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="ListModelSummaries", version=9, params=_params
        )
        _params["all"] = all_
        _params["user-tag"] = user_tag
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(UserModelList)
    async def ListModels(self, tag=None):
        """ListModels returns the models that the specified user
        has access to in the current server.  Controller admins (superuser)
        can list models for any user.  Other users
        can only ask about their own models.

        tag : str
        Returns -> UserModelList
        """
        if tag is not None and not isinstance(tag, (bytes, str)):
            raise Exception(f"Expected tag to be a str, received: {type(tag)}")

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="ModelManager", request="ListModels", version=9, params=_params)
        _params["tag"] = tag
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelDefaultsResults)
    async def ModelDefaultsForClouds(self, entities=None):
        """ModelDefaultsForClouds returns the default config values for the specified
        clouds.

        entities : typing.Sequence[~Entity]
        Returns -> ModelDefaultsResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager",
            request="ModelDefaultsForClouds",
            version=9,
            params=_params,
        )
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelInfoResults)
    async def ModelInfo(self, entities=None):
        """ModelInfo returns information about the specified models.

        entities : typing.Sequence[~Entity]
        Returns -> ModelInfoResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(type="ModelManager", request="ModelInfo", version=9, params=_params)
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ModelStatusResults)
    async def ModelStatus(self, entities=None):
        """ModelStatus returns a summary of the model.

        entities : typing.Sequence[~Entity]
        Returns -> ModelStatusResults
        """
        if entities is not None and not isinstance(entities, (bytes, str, list)):
            raise Exception(
                f"Expected entities to be a Sequence, received: {type(entities)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="ModelStatus", version=9, params=_params
        )
        _params["entities"] = entities
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ErrorResults)
    async def ModifyModelAccess(self, changes=None):
        """ModifyModelAccess changes the model access granted to users.

        changes : typing.Sequence[~ModifyModelAccess]
        Returns -> ErrorResults
        """
        if changes is not None and not isinstance(changes, (bytes, str, list)):
            raise Exception(
                f"Expected changes to be a Sequence, received: {type(changes)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="ModifyModelAccess", version=9, params=_params
        )
        _params["changes"] = changes
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ErrorResults)
    async def SetModelDefaults(self, config=None):
        """SetModelDefaults writes new values for the specified default model settings.

        config : typing.Sequence[~ModelDefaultValues]
        Returns -> ErrorResults
        """
        if config is not None and not isinstance(config, (bytes, str, list)):
            raise Exception(
                f"Expected config to be a Sequence, received: {type(config)}"
            )

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="SetModelDefaults", version=9, params=_params
        )
        _params["config"] = config
        reply = await self.rpc(msg)
        return reply

    @ReturnMapping(ErrorResults)
    async def UnsetModelDefaults(self, keys=None):
        """UnsetModelDefaults removes the specified default model settings.

        keys : typing.Sequence[~ModelUnsetKeys]
        Returns -> ErrorResults
        """
        if keys is not None and not isinstance(keys, (bytes, str, list)):
            raise Exception(f"Expected keys to be a Sequence, received: {type(keys)}")

        # map input types to rpc msg
        _params = dict()
        msg = dict(
            type="ModelManager", request="UnsetModelDefaults", version=9, params=_params
        )
        _params["keys"] = keys
        reply = await self.rpc(msg)
        return reply
