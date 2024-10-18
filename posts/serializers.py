from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
            'Image size larger then 2mb!')

        if value.image.width > 4096:
            raise serializers.ValidationError(
            'Image size larger then 4096px!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
            'Image height larger then 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'created_at', 'updated_at',
            'content', 'image','owner','is_owner', 'profile_id','profile_image',
            'image_filter',
        ]