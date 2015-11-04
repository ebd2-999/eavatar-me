# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import time
import logging

from avashell.base.shell import ShellBase, STR_EXIT, STR_OPEN_HELP

_logger = logging.getLogger(__name__)


class Shell(ShellBase):

    def __init__(self):
        super(Shell, self).__init__()
        self._interrupted = False

    def _terminate(self):
        self._interrupted = True
        sys.exit(0)

    def _run(self):
        while not self._interrupted:
            try:
                time.sleep(0.1)
                self.process_idle_tasks()
            except KeyboardInterrupt:
                _logger.info("Interrupted.")
                break

if __name__ == '__main__':
    shell = Shell()
    shell.run()