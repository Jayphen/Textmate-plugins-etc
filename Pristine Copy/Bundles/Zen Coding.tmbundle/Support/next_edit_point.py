#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zencoding import zen_core as zen_coding
from zen_editor import ZenEditor

editor = ZenEditor()
zen_coding.run_action('next_edit_point', editor)