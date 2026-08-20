from pathlib import Path
from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from biscuit.cli.cli import cli, setup


class TestCLI:
    def setup_method(self):
        setup()

    def test_version_option(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "Biscuit v" in result.output

    def test_help_option(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Biscuit CLI" in result.output

    @patch("biscuit.cli.cli.get_app_instance")
    def test_open_file_path(self, mock_get_app):
        mock_app = MagicMock()
        mock_get_app.return_value = mock_app

        runner = CliRunner()
        result = runner.invoke(cli, ["README.md"])
        assert result.exit_code == 0
        mock_get_app.assert_called_once()
        _, kwargs = mock_get_app.call_args
        assert kwargs["open_path"] == str(Path("README.md").resolve())
        mock_app.run.assert_called_once()

    @patch("biscuit.cli.cli.get_app_instance")
    def test_open_directory_path(self, mock_get_app):
        mock_app = MagicMock()
        mock_get_app.return_value = mock_app

        runner = CliRunner()
        result = runner.invoke(cli, ["src"])
        assert result.exit_code == 0
        mock_get_app.assert_called_once()
        _, kwargs = mock_get_app.call_args
        assert kwargs["open_path"] == str(Path("src").resolve())
        mock_app.run.assert_called_once()

    @patch("biscuit.cli.cli.get_app_instance")
    def test_open_command(self, mock_get_app):
        mock_app = MagicMock()
        mock_get_app.return_value = mock_app

        runner = CliRunner()
        result = runner.invoke(cli, ["open", "README.md"])
        assert result.exit_code == 0
        mock_get_app.assert_called_once()
        mock_app.open.assert_called_once()

    @patch("biscuit.cli.cli.get_app_instance")
    def test_goto_command(self, mock_get_app):
        mock_app = MagicMock()
        mock_get_app.return_value = mock_app

        runner = CliRunner()
        result = runner.invoke(cli, ["goto", "README.md", "10:5"])
        assert result.exit_code == 0
        mock_get_app.assert_called_once()
        mock_app.goto_location.assert_called_once()

    def test_invalid_option_raises_error(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--nonexistent-flag"])
        assert result.exit_code != 0
        assert "No such option" in result.output or "Error" in result.output
