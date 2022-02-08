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

# Generated by Django 1.11.24 on 2019-10-03 20:47
import django.db.models.deletion
from django.db import migrations, models


def migrate_old_sla(apps, schema_editor):
    from itsm.service.models import Service

    try:
        print('migrate_old_sla: reset to none')
        Service._objects.all().update(sla=None)
    except Exception as e:
        print('migrate_old_sla: {}'.format(e))


class Migration(migrations.Migration):

    dependencies = [
        ('sla', '__first__'),
        ('service', '0011_auto_20190919_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictdata',
            name='is_builtin',
            field=models.BooleanField(
                default=False, verbose_name='\u662f\u5426\u5185\u7f6e\uff08\u4e0d\u53ef\u5220\u9664\uff09'
            ),
        ),
        migrations.AddField(
            model_name='sysdict',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a'),
        ),
        migrations.AlterField(
            model_name='dictdata',
            name='is_readonly',
            field=models.BooleanField(
                default=False, verbose_name='\u662f\u5426\u53ea\u8bfb\uff08\u4e0d\u53ef\u7f16\u8f91\uff09'
            ),
        ),
        # foreign key constraint fails
        migrations.RunPython(migrate_old_sla),
        migrations.AlterField(
            model_name='service',
            name='sla',
            field=models.ForeignKey(
                help_text='\u5173\u8054\u7684\u670d\u52a1\u7ea7\u522b',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='sla_services',
                to='sla.Sla',
            ),
        ),
    ]
