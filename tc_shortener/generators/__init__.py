# -*- coding: utf-8 -*-

# Copyright (c) 2015, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.


class BaseGenerator(object):

    def __init__(self, context):
        self.context = context
