# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

"""
Entry-point for command-line interface.
"""

import avacli.cmds
from avacli.cmds.cli import cli


def main():
    return cli(auto_envvar_prefix=b'AVA')


if __name__ == '__main__':
    main()
