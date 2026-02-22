from src.main import main


def test_main_runs(capsys):
    main()
    out = capsys.readouterr().out
    assert "initialized" in out
