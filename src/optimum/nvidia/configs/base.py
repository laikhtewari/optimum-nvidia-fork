#  coding=utf-8
#  Copyright 2023 The HuggingFace Inc. team. All rights reserved.
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#      http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from collections import UserDict
from typing import Protocol, Any, Mapping


class ModelConfig(Protocol):

    @property
    def vocab_size(self) -> int:
        ...

    @property
    def max_sequence_length(self) -> int:
        ...

    @property
    def hidden_size(self) -> int:
        ...

    @property
    def intermediate_size(self) -> int:
        ...

    @property
    def num_layers(self) -> int:
        ...

    @property
    def num_heads(self) -> int:
        ...

    @property
    def use_multi_query_attention(self) -> bool:
        ...

    @property
    def activation(self) -> str:
        ...

    @property
    def num_kv_heads(self) -> int:
        return 1 if self.use_multi_query_attention else self.num_heads


class TransformersConfig(UserDict, ModelConfig):

    __slots__ = ("_config", )

    def __init__(self, pretrained_config: Mapping[str, Any]):
        super().__init__(pretrained_config)

    @property
    def vocab_size(self) -> int:
        return self.data["vocab_size"]

    @property
    def max_sequence_length(self) -> int:
        return self.data["max_sequence_length"]

    @property
    def hidden_size(self) -> int:
        return self.data["hidden_size"]

    @property
    def intermediate_size(self) -> int:
        return self.data["intermediate_size"]

    @property
    def num_layers(self) -> int:
        return self.data["num_hidden_layers"]

    @property
    def num_heads(self) -> int:
        return self.data["num_attention_heads"]

    @property
    def use_multi_query_attention(self) -> bool:
        return self.get("num_key_value_heads", self.num_heads) == 1

    @property
    def activation(self) -> str:
        return self.data["hidden_act"]

