# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 1.11.24 on 2019-11-15 13:29
from __future__ import unicode_literals

import django.db.models.deletion
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0029_auto_20191114_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlaActionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(db_index=True, verbose_name='任务ID')),
                (
                    'status',
                    models.CharField(
                        choices=[('SUCCESS', '成功'), ('FAILED', '失败')], max_length=255, verbose_name='结果状态'
                    ),
                ),
                ('action_type', models.CharField(max_length=255, verbose_name='行为类型')),
                ('action_detail', jsonfield.fields.JSONField(default={}, verbose_name='行为详情')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='动作发生时间')),
                ('condition', jsonfield.fields.JSONField(default=[], verbose_name='触发的规则')),
            ],
            options={'verbose_name': 'sla行为历史记录', 'verbose_name_plural': 'sla行为历史记录', 'ordering': ('-create_time',),},
        ),
        migrations.CreateModel(
            name='SlaEventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(db_index=True, verbose_name='任务ID')),
                ('priority', models.CharField(max_length=255, verbose_name='优先级')),
                (
                    'event_type',
                    models.CharField(
                        choices=[('PAUSE', '暂停'), ('RESUME', '恢复'), ('STOP', '停止'), ('START', '启动')],
                        max_length=255,
                        verbose_name='事件类型',
                    ),
                ),
                ('is_archived', models.BooleanField(default=False, verbose_name='是否已归档')),
                (
                    'tick_flag',
                    models.CharField(
                        choices=[('START', '开始计时'), ('END', '结束计时'), ('KEEP', '保持')],
                        default='KEEP',
                        max_length=255,
                        verbose_name='计时标志',
                    ),
                ),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='事件发生时间')),
            ],
            options={'verbose_name': 'sla事件日志', 'verbose_name_plural': 'sla事件日志',},
        ),
        migrations.CreateModel(
            name='SlaTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'task_status',
                    models.CharField(
                        choices=[('UNACTIVATED', '未激活'), ('RUNNING', '计时中'), ('PAUSED', '暂停中'), ('STOPPED', '已停止')],
                        default='UNACTIVATED',
                        max_length=64,
                        verbose_name='任务状态',
                    ),
                ),
                ('is_frozen', models.BooleanField(default=False, verbose_name='是否冻结')),
                (
                    'sla_status',
                    models.CharField(
                        choices=[('NORMAL', '正常'), ('UPGRADED', '已升级'), ('VIOLATED', '已违规')],
                        default='NORMAL',
                        max_length=64,
                        verbose_name='sla状态',
                    ),
                ),
                ('deadline', models.DateTimeField(null=True, verbose_name='任务截止时间')),
                ('start_tick_time', models.DateTimeField(null=True, verbose_name='开始计时的时间')),
                ('last_tick_time', models.DateTimeField(null=True, verbose_name='最近一次检查时间')),
                ('stop_tick_time', models.DateTimeField(null=True, verbose_name='结束计时的时间')),
                ('cost_duration', models.IntegerField(default=0, verbose_name='经过的时长(s)')),
                ('archived_duration', models.IntegerField(default=0, verbose_name='归档的时长(s)')),
                ('cost_percent', models.IntegerField(default=0, verbose_name='经过的百分比(%)')),
                ('sla_id', models.IntegerField(verbose_name='关联的sla协议ID')),
                (
                    'ticket',
                    models.OneToOneField(
                        help_text='关联的单据',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='sla_task',
                        to='ticket.Ticket',
                    ),
                ),
            ],
            options={'verbose_name': 'sla任务', 'verbose_name_plural': 'sla任务',},
        ),
    ]
