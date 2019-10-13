from rest_framework import serializers
from rest_framework.utils import model_meta


class PhoenixModelSerializer(serializers.ModelSerializer):

    @classmethod
    def get_model(cls):
        model = cls.Meta.model
        if model is NotImplemented:
            raise NotImplementedError(
                "Serializer does not have a model defined")
        return model
