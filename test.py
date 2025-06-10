from click.testing import CliRunner
from main import summarize

def test_summary_output():
    runner = CliRunner()
    result = runner.invoke(summarize, ['logs/OpenStack_2k.log'])
    assert "Summary" in result.output
    assert "Errors" in result.output
