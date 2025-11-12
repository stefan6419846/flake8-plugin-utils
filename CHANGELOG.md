# Development version

* Refactor repository layout and build backend
* Increase test coverage
* Remove deprecated functionality.
* Drop support for Python < 3.10

# Version 1.3.3 - 2022-01-14

* add py.typed file (#78)

# Version 1.3.2 - 2021-05-05

* Drop noqa detection (#56)
* docs: Add help for Makefile

# Version 1.3.1 - 2020-08-06

* Fix handling of encoding when loading files (#37)

# Version 1.3.0 - 2020-03-26

* add `check_equivalent_nodes` utility function

# Version 1.2.0 - 2020-03-06

* add `config` argument to `assert_error` and `assert_not_error`

# Version 1.1.1 - 2020-03-02

* ignore encoding errors when reading strings for noqa validation

# Version 1.1.0 - 2020-03-01

* add ability for plugins to parse and use configuration
**NB: this change breaks type-checking if you use typing/mypy. Change your
code to inherit from `Plugin[None]` and `Visitor[None]` to fix.**

# Version 1.0.0 - 2019-05-23

* add message formatting to Error

# Version 0.2.1 - 2019-04-01

* don`t strip before src dedent in _error_from_src
* add is_none, is_true, is_false util functions

# Version 0.2.0 - 2019-02-21

* add assert methods

# Version 0.1.0 - 2019-02-09

* initial
