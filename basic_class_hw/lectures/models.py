from django.db import models

class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)  # 강의 ID (자동 증가)
    name = models.CharField(max_length=255, null=False)  # 강의 이름
    instructor_id = models.IntegerField(null=False)  # 강사 ID
    is_online = models.BooleanField(null=False)  # 온/오프라인 여부
    prerequisite = models.CharField(max_length=255, blank=True, null=True)  # 사전 강의

    def __str__(self):
        return self.name
