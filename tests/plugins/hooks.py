from typing import List
import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.python import Function


def pytest_configure(config: Config) -> None:
    """Enable verbose and output when running tests. Simulate `-v` and `-s` option in a command line."""

    config.option.verbose = 1
    config.option.capture = "yes"


def pytest_report_header(config: Config) -> List[str]:
    """Add information to test report header."""

    if config.option.verbose > 0:
        return ["Project: yFox flask blog", "Written by: Volodymyr Yahello"]


def pytest_addoption(parser: Parser) -> None:
    """Add custom parameters."""

    parser.addoption(
        "--skip-markers", "-S", nargs="*", action="store", default=None, help="skip test(s) with certain marker.",
    )

    parser.addoption(
        "--use-fixtures", "-U", nargs="*", action="store", default=None, help="Run test that use a specific fixture",
    )


def pytest_runtest_setup(item: Function) -> None:
    """Skip tests that belong to specific marker with ``--skip-marker`` cmd option."""

    markers: str = item.config.getvalue("skip_markers")

    if markers:
        for marker in markers:
            if marker in item.keywords:
                pytest.skip(f"Skipping [@{marker}] pytest marker")


def pytest_collection_modifyitems(items: List[Function], config: Config) -> None:
    fixtures: str = config.getoption("use_fixtures")

    if fixtures:
        selected_tests: List = []
        deselected_tests: List = []

        for fixture in fixtures:
            if fixture:
                for test in items:
                    if fixture in test.fixturenames:
                        selected_tests.append(test)
                    else:
                        deselected_tests.append(test)

        config.hook.pytest_deselected(items=deselected_tests)
        items[:] = selected_tests
