from rest_framework import serializers
from .models import Tag, Entry
from django.contrib.auth import get_user_model

User = get_user_model()

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        field = ["id", "name"]

class EntrySerializers(serializers.ModelSerializer):
    tags = TagSerializers(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        write_only=True,
        source="tags"
    )