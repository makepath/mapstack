from django_celery_results.models import TaskResult
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField("get_result")

    class Meta:
        model = TaskResult
        fields = [
            "task_id",
            "status",
            "result",
        ]

    def get_result(self, obj):
        if obj.status == "SUCCESS":
            return obj.result
        return
