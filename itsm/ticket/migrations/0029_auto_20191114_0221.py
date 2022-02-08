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

    dependencies = [
        ('ticket', '0028_auto_20191113_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusTransitLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_status', models.CharField(max_length=255, verbose_name='流转前的单据状态')),
                ('to_status', models.CharField(max_length=255, verbose_name='流转后的单据状态')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={'verbose_name': '单据状态流转日志', 'verbose_name_plural': '单据状态流转日志',},
        ),
        migrations.RemoveField(model_name='ticketcommentinvite', name='number',),
        migrations.AddField(
            model_name='status', name='meta', field=jsonfield.fields.JSONField(default={}, verbose_name='配置信息'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='pre_status',
            field=models.CharField(default='', max_length=32, verbose_name='单据前一状态'),
        ),
        migrations.AddField(
            model_name='ticketcommentinvite',
            name='notify_type',
            field=models.CharField(
                choices=[('WEIXIN', '微信'), ('EMAIL', '邮箱'), ('SMS', '短信')],
                default='SMS',
                max_length=32,
                verbose_name='通知方式',
            ),
        ),
        migrations.AddField(
            model_name='ticketcommentinvite',
            name='receiver',
            field=models.CharField(default='', max_length=64, verbose_name='联系人/联系方式'),
        ),
        migrations.AddField(
            model_name='ticketfield',
            name='source',
            field=models.CharField(
                choices=[('CUSTOM', '自定义添加'), ('TABLE', '基础模型添加')], default='CUSTOM', max_length=32, verbose_name='添加方式'
            ),
        ),
        migrations.AddField(
            model_name='ticketfield',
            name='workflow_field_id',
            field=models.IntegerField(default=-1, verbose_name='流程版本字段ID'),
        ),
        migrations.AlterField(
            model_name='status', name='fields', field=jsonfield.fields.JSONField(default=[], verbose_name='字段列表'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(
                choices=[
                    ('WAIT', '待处理'),
                    ('RUNNING', '处理中'),
                    ('QUEUEING', '后台处理中'),
                    ('RECEIVING', '待认领'),
                    ('DISTRIBUTING', '待分派'),
                    ('TERMINATED', '被终止'),
                    ('FINISHED', '已结束'),
                    ('FAILED', '执行失败'),
                    ('SUSPEND', '被挂起'),
                ],
                default='WAIT',
                max_length=32,
                verbose_name='节点状态',
            ),
        ),
        migrations.AlterField(
            model_name='ticket', name='current_status', field=models.CharField(max_length=32, verbose_name='单据状态'),
        ),
        migrations.AlterField(
            model_name='ticket', name='title', field=models.CharField(max_length=128, verbose_name='单据名称'),
        ),
        migrations.AlterField(
            model_name='ticketfield',
            name='source_type',
            field=models.CharField(
                choices=[('CUSTOM', '自定义数据'), ('API', '接口数据'), ('DATADICT', '数据字典'), ('RPC', 'RPC数据')],
                default='CUSTOM',
                max_length=32,
                verbose_name='数据来源类型',
            ),
        ),
        migrations.AlterField(
            model_name='ticketstatedraft',
            name='draft',
            field=jsonfield.fields.JSONField(blank=True, default=[], null=True, verbose_name='单据节点草稿字段'),
        ),
        migrations.AddField(
            model_name='statustransitlog',
            name='ticket',
            field=models.ForeignKey(
                help_text='关联的单据',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='transit_log',
                to='ticket.Ticket',
            ),
        ),
    ]
