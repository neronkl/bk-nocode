# Generated by Django 3.2.4 on 2022-02-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("iadmin", "0015_auto_20210318_1041"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customnotice",
            name="action",
            field=models.CharField(
                choices=[
                    ("TERMINATE", "单据终止通知"),
                    ("FOLLOW", "邀请关注通知"),
                    ("INVITE", "邀请评价通知"),
                    ("SUPERVISE", "单据督办通知"),
                    ("SUSPEND", "单据挂起通知"),
                    ("UNSUSPEND", "单据恢复通知"),
                    ("TRANSITION", "单据待办通知"),
                    ("WAITING_FOR_OPERATE", "任务待办通知"),
                    ("WAITING_FOR_CONFIRM", "任务待总结通知"),
                    ("NOTIFY_FOLLOWER", "关注人通知"),
                    ("FINISHED", "单据结束通知"),
                ],
                default="default",
                max_length=32,
                verbose_name="通知模板类型",
            ),
        ),
    ]
