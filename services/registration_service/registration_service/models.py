from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255, unique=True)  # 学校名称

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=100)  # 姓名
    student_id = models.CharField(max_length=50)  # 学号
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="registrations")  # 学校
    teacher_name = models.CharField(max_length=100)  # 指导老师
    teacher_phone = models.CharField(max_length=15)  # 指导老师手机号码
    created_at = models.DateTimeField(auto_now_add=True)  # 报名时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间

    def __str__(self):
        return f"{self.name} - {self.school.name}"


class Competition(models.Model):
    name = models.CharField(max_length=255)  # 比赛名称
    description = models.TextField()  # 比赛描述
    start_date = models.DateField()  # 比赛开始时间
    end_date = models.DateField()  # 比赛结束时间
    registration_deadline = models.DateField()  # 报名截止时间

    def __str__(self):
        return self.name