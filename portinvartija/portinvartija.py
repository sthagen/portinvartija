# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""API of interface operations for data driven topics.."""
import os
import sys
from typing import List, Union

import kdl  # type: ignore
from first import first


def it_starts_with_silence() -> None:
    """Stub to bootstrap development and survive the make rounds before implementation is in place."""
    assert os.getenv('DO_NOT_COMPLAIN_IF_THIS_IS_PRESENT_IN_YOUR_ENV', 'all good') == 'all good'  # nosec B101
    assert sys.path > []  # nosec B101
    doc = kdl.Document()
    doc.append(
        kdl.Node(
            name='simple-name',
            properties=None,
            arguments=[123],
            children=[
                kdl.Node(
                    name='complex name here!',
                    properties=None,
                    arguments=None,
                    children=None,
                )
            ],
        )
    )
    ast = kdl.parse(doc)
    assert next(ast[0]) == 123  # nosec B101
    assert first((1, 2)) == 1  # nosec B101


def main(argv: Union[List[str], None] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    return 0
