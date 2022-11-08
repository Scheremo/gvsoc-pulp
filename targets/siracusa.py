#
# Copyright (C) 2020 ETH Zurich and University of Bologna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pulp.chips.siracusa.pulp_open_board import Pulp_open_board


class Target(Pulp_open_board):
    """
    Pulp-open board

    """

    def __init__(self, options):

        super(Target, self).__init__(
            options=options
        )


    def __str__(self) -> str:
        return "Pulp-open virtual board"