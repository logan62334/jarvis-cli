#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import cast

import click
from click import Group

from jarvis.cli.src.jarvis import run


@click.group(invoke_without_command=False)
def jarvis():
    print("========智能抢菜服务========")


cast(Group, jarvis).add_command(run)
