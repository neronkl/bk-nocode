# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-NOCODE SMAKER蓝鲸无代码平台  available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-NOCODE 蓝鲸无代码平台(S-maker) is licensed under the MIT License.

License for BK-NOCODE 蓝鲸无代码平台(S-maker) :
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
from rest_framework.routers import DefaultRouter

from nocode.project_manager.views.operate_log import OperateLogViewSet
from nocode.project_manager.views.project_manager import ProjectManagerViewSet
from nocode.project_manager.views.project_version import ProjectVersionViewSet
from nocode.project_manager.views.system_user import SuperUserViewSet
from nocode.project_manager.views.project_white import ProjectWhiteViewSet

routers = DefaultRouter(trailing_slash=True)

routers.register(r"manager", ProjectManagerViewSet, basename="project_manager")
routers.register(r"version", ProjectVersionViewSet, basename="project_version")
routers.register(r"operate_log", OperateLogViewSet, basename="operate_log")
routers.register(r"system_user", SuperUserViewSet, basename="system_user")
routers.register(r"project_white", ProjectWhiteViewSet, basename="project_white")

urlpatterns = routers.urls
