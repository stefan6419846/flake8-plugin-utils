import ast


def _is(node: ast.AST, value: object) -> bool:
    return isinstance(node, ast.Constant) and node.value is value


def is_none(node: ast.AST) -> bool:
    return _is(node, None)


def is_false(node: ast.AST) -> bool:
    return _is(node, False)


def is_true(node: ast.AST) -> bool:
    return _is(node, True)
