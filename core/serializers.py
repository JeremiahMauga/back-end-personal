from rest_framework.serializers import ModelSerializer, StringRelatedField, SerializerMethodField, PrimaryKeyRelatedField, CharField
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from core.models import Inventory

## Serializes new user sign ups that responds with the new user's information including a new token.
class UserSerializerWithToken(ModelSerializer):

    token = SerializerMethodField()
    password = CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['token', 'username', 'password']

# Inventory Serializer
class InventorySerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'game_title', 'voter', 'votes')

## Serializes current user
class UserSerializer(ModelSerializer):
    inventory = InventorySerializer(many=True)

    class Meta:
        model = User
        fields = ['id','username','inventory']