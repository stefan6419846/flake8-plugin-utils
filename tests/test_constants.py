import ast

import pytest

from flake8_plugin_utils.utils import constants


@pytest.mark.parametrize(
    ("expression", "func", "expected"),
    [
        # is_true
        ("True", constants.is_true, True),
        ("False", constants.is_true, False),
        ("5", constants.is_true, False),
        ("None", constants.is_true, False),
        # is_false
        ("False", constants.is_false, True),
        ("True", constants.is_false, False),
        ("5", constants.is_false, False),
        ("None", constants.is_false, False),
        # is_none
        ("None", constants.is_none, True),
        ("False", constants.is_none, False),
        ("5", constants.is_none, False),
        ("True", constants.is_none, False),
    ],
)
def test_equivalent_nodes(expression, func, expected):
    body = ast.parse(expression).body[0]
    assert isinstance(body, ast.Expr)
    node = body.value
    assert func(node) is expected
