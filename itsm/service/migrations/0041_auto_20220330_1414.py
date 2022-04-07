# Generated by Django 3.2.4 on 2022-03-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0040_alter_service_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkSheetEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creator", models.CharField(max_length=64, verbose_name="创建人")),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(max_length=64, verbose_name="修改人")),
                ("end_at", models.DateTimeField(null=True, verbose_name="结束时间")),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="是否软删除"),
                ),
                ("is_builtin", models.BooleanField(default=False, verbose_name="是否内置")),
                (
                    "project_key",
                    models.CharField(default=0, max_length=32, verbose_name="项目key"),
                ),
                ("worksheet_id", models.IntegerField(verbose_name="表单ID")),
                ("service_id", models.IntegerField(verbose_name="服务ID")),
                (
                    "action_type",
                    models.CharField(
                        choices=[("ADD", "增加记录"), ("EDIT", "更新记录"), ("DEL", "删除记录")],
                        max_length=32,
                        verbose_name="触发类型",
                    ),
                ),
                ("conditions", models.JSONField(default=[], verbose_name="触发条件")),
                ("params", models.JSONField(default={}, verbose_name="触发参数，默认{id}")),
            ],
            options={
                "verbose_name": "服务表单触发任务配置表",
                "verbose_name_plural": "服务表单触发任务配置表",
            },
        ),
        migrations.AddField(
            model_name="service",
            name="rule_type",
            field=models.CharField(
                choices=[
                    ("NO_RULE", "无触发规则"),
                    ("PERIOD", "周期触发"),
                    ("WORKSHEET_RECORD", "记录更新触发"),
                ],
                default="",
                max_length=64,
                verbose_name="自动化触发规则类型",
            ),
        ),
    ]