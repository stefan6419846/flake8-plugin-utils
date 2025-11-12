# flake8-plugin-utils

The package provides base classes and utils for flake8 plugin writing.

## Installation

```bash
pip install flake8-plugin-utils
```

## Example

Write simple plugin

```python
from flake8_plugin_utils import Error, Visitor, Plugin

class MyError(Error):
    code = 'X100'
    message = 'my error'

class MyVisitor(Visitor):
    def visit_ClassDef(self, node):
        self.error_from_node(MyError, node)

class MyPlugin(Plugin):
    name = 'MyPlugin'
    version = '0.1.0'
    visitors = [MyVisitor]
```

and test it with pytest

```python
from flake8_plugin_utils import assert_error, assert_not_error

def test_code_with_error():
    assert_error(MyVisitor, 'class Y: pass', MyError)

def test_code_without_error():
    assert_not_error(MyVisitor, 'x = 1')
```

### Configuration

To add configuration to a plugin, do the following:

1. Implement classmethod `add_options` in your plugin class, as per the [flake8 docs](https://flake8.pycqa.org/en/latest/plugin-development/plugin-parameters.html#registering-options).
2. Override classmethod `parse_options_to_config` in your plugin class to return any object holding the options you need.
3. If you need a custom `__init__` for your visitor, make sure it accepts a keyword argument named `config` and pass it to `super().__init__`
4. Use `self.config` in visitor code.

Example:

```python
from flake8_plugin_utils import Error, Visitor, Plugin, assert_error

class MyError(Error):
    code = 'X100'
    message = 'my error with {thing}'

class MyConfig:
    def __init__(self, config_option):
        self.config_option = config_option

class MyVisitorWithConfig(Visitor):
    def visit_ClassDef(self, node):
        self.error_from_node(
            MyError, node, thing=f'{node.name} {self.config.config_option}'
        )

class MyPluginWithConfig(Plugin):
    name = 'MyPluginWithConfig'
    version = '0.0.1'
    visitors = [MyVisitorWithConfig]

    @classmethod
    def add_options(cls, options_manager):
        options_manager.add_option('--config_option', parse_from_config=True, ...)

    @classmethod
    def parse_options_to_config(cls, option_manager, options, args):
        return MyConfig(config_option=options.config_option)


def test_code_with_error():
    assert_error(
        MyVisitorWithConfig,
        'class Y: pass',
        MyError,
        config=MyConfig(config_option='123'),
        thing='Y 123',
    )
```

### Formatting

Your `Error`s can take formatting arguments in their `message`:

```python
from flake8_plugin_utils import Error, Visitor, assert_error

class MyFormattedError(Error):
    code = 'X101'
    message = 'my error with {thing}'

class MyFormattedVisitor(Visitor):
    def visit_ClassDef(self, node):
        self.error_from_node(MyFormattedError, node, thing=node.name)

def test_code_with_error():
    assert_error(
        MyFormattedVisitor,
        'class Y: pass',
        MyFormattedError,
        thing='Y',
    )
```

### Usage with typing/mypy

The `Plugin` and `Visitor` classes are generic with the config class as type
parameter.  If your plugin does not have any config, inherit it from
`Plugin[None]` and the visitors from `Visitor[None]`.  Otherwise, use the
config class as the type parameter (e.g. `Plugin[MyConfig]` and
`Visitor[MyConfig]` in the above example).

### Utility functions

* `assert_error`, `assert_not_error`
Utilities for testing visitors (see examples above).

* `is_true`, `is_false`, `is_none`
Convenience functions to check if an AST node represents a
`True`/`False`/`None` value.

* `check_equivalent_nodes`
Checks if two given AST nodes are equivalent.
The nodes are considered equivalent in the following cases:
  * dicts -- if they contain same key-value pairs, possibly in different order,
  with duplicates and `**expansions` taken into account
  * sets -- if they contain same elements, possibly in different order,
  with duplicates taken into account
  * anything else -- if they represent the same AST, regardless of formatting
  (with any dicts in sets inside checked according to the rules above)
