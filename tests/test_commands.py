from unittest import mock

import pytest
from json2table.commands import app
from typer.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


def test_head(monkeypatch, runner: CliRunner):
    mock_df = mock.Mock()
    mock_read = mock.Mock()
    mock_read.return_value = mock_df
    monkeypatch.setattr("json2table.commands.pd.read_json", mock_read)

    runner.invoke(app, ["head", "test.json", "--n", "5"])

    mock_read.assert_called_with("test.json")
    mock_df.head.assert_called_once_with(5)


def test_convert(monkeypatch, runner: CliRunner):
    mock_df = mock.Mock()
    mock_read = mock.Mock()
    mock_read.return_value = mock_df
    monkeypatch.setattr("json2table.commands.pd.read_json", mock_read)

    runner.invoke(app, ["convert", "test.json", "--t", "xlsx"])

    mock_read.assert_called_with("test.json")
    mock_df.to_excel.assert_called_once_with("test.xlsx", index=False)

    result = runner.invoke(app, ["convert", "test.json", "--t", "exe"])
    assert result.stdout == 'Option t should be one of ["csv", "xlsx"]\n'
