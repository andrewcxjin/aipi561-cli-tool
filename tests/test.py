from click.testing import CliRunner
from main import summarize

def test_summarize():
    runner = CliRunner()

    test_log_content = ""

    with runner.isolated_filesystem():
        with open("test.log", "w") as f:
            f.write(test_log_content)

        result = runner.invoke(summarize, ["test.log"])

        assert result.exit_code == 0
        assert "Summary of test.log" in result.output
        assert "Info messages: 2" in result.output
        assert "Warnings: 1" in result.output
        assert "Errors: 1" in result.output

        assert "Sample Info:" in result.output
        assert "Sample Warning:" in result.output
        assert "Sample Error:" in result.output

