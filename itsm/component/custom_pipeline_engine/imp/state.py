# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from typing import Optional, Dict, List

from django.utils import timezone
from bamboo_engine.eri import State
from bamboo_engine import metrics
from bamboo_engine.utils.string import unique_id
from bamboo_engine.exceptions import StateVersionNotMatchError

from pipeline.eri.models import State as DBState


class StateMixin:
    @metrics.setup_histogram(metrics.ENGINE_RUNTIME_STATE_READ_TIME)
    def get_state(self, node_id: str) -> State:
        """
        获取某个节点的状态对象

        : param node_id: 节点 ID
        : type node_id: str
        : return: State 实例
        : rtype: State
        """
        if not hasattr(self.local, "states"):
            return None
        value = self.local.states.get(node_id)
        if value is None:
            return None
        state = DBState(**value)

        return State(
            node_id=state.node_id,
            root_id=state.root_id,
            parent_id=state.parent_id,
            name=state.name,
            version=state.version,
            loop=state.loop,
            inner_loop=state.inner_loop,
            retry=state.retry,
            skip=state.skip,
            error_ignored=state.error_ignored,
            created_time=state.created_time,
            started_time=state.started_time,
            archived_time=state.archived_time,
        )

    @metrics.setup_histogram(metrics.ENGINE_RUNTIME_STATE_READ_TIME)
    def get_state_or_none(self, node_id: str) -> Optional[State]:
        """
        获取某个节点的状态对象，如果不存在则返回 None

        : param node_id: 节点 ID
        : type node_id: str
        : return: State 实例
        : rtype: State
        """
        try:
            return self.get_state(node_id)
        except DBState.DoesNotExist:
            return None

    def get_state_by_root(self, root_id: str) -> List[State]:
        """
        根据根节点 ID 获取一批节点状态

        :param root_id: 根节点 ID
        :type root_id: str
        :return: 节点状态列表
        :rtype: List[State]
        """
        pass

    def get_state_by_parent(self, parent_id: str) -> List[State]:
        """
        根据父节点 ID 获取一批节点状态

        :param parent_id: 父节点 ID
        :type parent_id: str
        :return: 节点状态列表
        :rtype: List[State]
        """
        pass

    def batch_get_state_name(self, node_id_list: List[str]) -> Dict[str, str]:
        """
        批量获取一批节点的状态

        :param node_id_list: 节点 ID 列表
        :type node_id_list: List[str]
        :return: 节点ID -> 状态名称
        :rtype: Dict[str, str]
        """
        data = {}
        for node_id, state in self.local.states.items():
            if node_id in node_id_list:
                data[node_id] = state["name"]

        return data

    def has_state(self, node_id: str) -> bool:
        """
        是否存在某个节点的的状态

        :param node_id: 节点 ID
        :type node_id: str
        :return: 该节点状态是否存在
        :rtype: bool
        """
        pass

    def reset_state_inner_loop(self, node_id: str) -> int:
        """
        设置节点的当前流程重入次数

        :param node_id: 节点 ID
        :type node_id: str
        :return: 更新状态行数
        :rtype: int
        """
        pass

    def reset_children_state_inner_loop(self, node_id: str) -> int:
        """
        批量设置子流程节点的所有子节点inner_loop次数

        :param node_id: 子流程节点 ID
        :type node_id: str
        :return: 更新状态行数
        :rtype: int
        """
        pass

    def set_state_root_and_parent(self, node_id: str, root_id: str, parent_id: str):
        """
        设置节点的根流程和父流程 ID

        :param node_id: 节点 ID
        :type node_id: str
        :param root_id: 根流程 ID
        :type root_id: str
        :param parent_id: 父流程 ID
        :type parent_id: str
        """
        pass

    @metrics.setup_histogram(metrics.ENGINE_RUNTIME_STATE_WRITE_TIME)
    def set_state(
        self,
        node_id: str,
        to_state: str,
        version: str = None,
        loop: int = -1,
        inner_loop: int = -1,
        root_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        is_retry: bool = False,
        is_skip: bool = False,
        reset_retry: bool = False,
        reset_skip: bool = False,
        error_ignored: bool = False,
        reset_error_ignored: bool = False,
        refresh_version: bool = False,
        clear_started_time: bool = False,
        set_started_time: bool = False,
        clear_archived_time: bool = False,
        set_archive_time: bool = False,
    ) -> str:
        """
        设置节点的状态，如果节点存在，进行状态转换时需要满足状态转换状态机

        :param node_id: 节点 ID
        :type node_id: str
        :param to_state: 目标状态
        :type to_state: str
        :param loop: 循环次数, 为 -1 时表示不设置
        :type loop: int, optional
        :param inner_loop: 当前流程循环次数, 为 -1 时表示不设置
        :type inner_loop: int, optional
        :param version: 目标状态版本，为空时表示不做版本校验
        :type version: Optional[str], optional
        :param root_id: 根节点 ID，为空时表示不设置
        :type root_id: Optional[str], optional
        :param parent_id: 父节点 ID，为空时表示不设置
        :type parent_id: Optional[str], optional
        :param is_retry: 是否增加重试次数
        :type is_retry: bool, optional
        :param is_skip: 是否将跳过设置为 True
        :type is_skip: bool, optional
        :param reset_retry: 是否重置重试次数
        :type reset_retry: bool, optional
        :param reset_skip: 是否重置跳过标志
        :type reset_skip: bool, optional
        :param error_ignored: 是否为忽略错误跳过
        :type error_ignored: bool, optional
        :param reset_error_ignored: 是否重置忽略错误标志
        :type reset_error_ignored: bool, optional
        :param refresh_version: 是否刷新版本号
        :type refresh_version: bool, optional
        :param clear_started_time: 是否清空开始时间
        :type clear_started_time: bool, optional
        :param set_started_time: 是否设置开始时间
        :type set_started_time: bool, optional
        :param clear_archived_time: 是否清空归档时间
        :type clear_archived_time: bool, optional
        :param set_archive_time: 是否设置归档时间
        :type set_archive_time: bool, optional
        :return: 该节点最新版本
        :rtype: str
        """
        state = self.get_state_or_none(node_id)

        if state and version and state.version != version:
            raise StateVersionNotMatchError(
                "state version({}) not match {}".format(state.version, version)
            )

        fields = {}

        if loop != -1:
            fields["loop"] = loop

        if inner_loop != -1:
            fields["inner_loop"] = inner_loop

        if root_id:
            fields["root_id"] = root_id

        if parent_id:
            fields["parent_id"] = parent_id

        if is_retry and state:
            fields["retry"] = state.retry + 1

        if is_skip and state:
            fields["skip"] = True

        if reset_retry and state:
            fields["retry"] = 0

        if reset_skip and state:
            fields["skip"] = False

        if reset_error_ignored and state:
            fields["error_ignored"] = False

        if error_ignored and state:
            fields["error_ignored"] = True

        if refresh_version or state is None:
            fields["version"] = unique_id("v")

        if clear_started_time and state:
            fields["started_time"] = None

        if set_started_time:
            fields["started_time"] = timezone.now()

        if clear_archived_time and state:
            fields["archived_time"] = timezone.now()

        if set_archive_time:
            fields["archived_time"] = timezone.now()

        if state:
            self.local.states.get(node_id).update(name=to_state, **fields)
            ret_version = fields.get("version", state.version)
        else:
            if hasattr(self.local, "states"):
                value = {"node_id": node_id, "name": to_state}
                value.update(fields)
                self.local.states[str(node_id)] = value
            else:
                value = {"node_id": node_id, "name": to_state}
                value.update(fields)
                states = {str(node_id): value}
                self.local.states = states
            ret_version = fields["version"]
        return ret_version
