# Generated by Django 3.2.4 on 2021-09-20 18:10

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import jsonfield.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PageComponent",
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
                (
                    "creator",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="创建人"
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                (
                    "updated_by",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="修改人"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="是否软删除"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FUNCTION", "功能组件"),
                            ("LIST", "列表组件"),
                            ("SHEET", "表单组件"),
                        ],
                        max_length=32,
                        verbose_name="表单组件/列表组件/功能卡片",
                    ),
                ),
                ("value", models.CharField(max_length=1000, verbose_name="组件绑定的值")),
                (
                    "layout",
                    models.CharField(
                        choices=[("COL_6", "半行"), ("COL_12", "整行")],
                        default="COL_6",
                        max_length=32,
                        verbose_name="字段布局",
                    ),
                ),
                ("config", jsonfield.fields.JSONField(verbose_name="页面配置")),
                ("page_id", models.IntegerField(verbose_name="页面id")),
            ],
            options={
                "verbose_name": "页面组件",
                "verbose_name_plural": "页面组件",
            },
        ),
        migrations.CreateModel(
            name="Page",
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
                (
                    "creator",
                    models.CharField(
                        blank=True,
                        default="system",
                        max_length=64,
                        null=True,
                        verbose_name="创建人",
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                (
                    "updated_by",
                    models.CharField(
                        blank=True,
                        default="system",
                        max_length=64,
                        null=True,
                        verbose_name="修改人",
                    ),
                ),
                (
                    "end_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="结束时间"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="是否软删除"
                    ),
                ),
                ("key", models.CharField(max_length=255, verbose_name="页面关键字")),
                ("name", models.CharField(max_length=64, verbose_name="页面名称")),
                (
                    "desc",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="页面描述"
                    ),
                ),
                ("order", models.IntegerField(default=1, verbose_name="节点顺序")),
                (
                    "icon",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="图标"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("FUNCTION", "功能卡片"), ("LIST", "列表"), ("SHEET", "表单")],
                        max_length=32,
                        verbose_name="页面类型",
                    ),
                ),
                (
                    "project_key",
                    models.CharField(default="0", max_length=32, verbose_name="项目"),
                ),
                (
                    "route",
                    jsonfield.fields.JSONField(default=[], verbose_name="前置路径集合"),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="page.page",
                        verbose_name="上级页面",
                    ),
                ),
            ],
            options={
                "verbose_name": "页面",
                "verbose_name_plural": "页面",
                "ordering": ("order",),
            },
            managers=[
                ("_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
