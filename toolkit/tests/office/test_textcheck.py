import importlib.util
from pathlib import Path

_PATH = Path(__file__).resolve().parents[3] / "keel" / "office" / "tools" / "textcheck.py"
_spec = importlib.util.spec_from_file_location("textcheck", _PATH)
textcheck = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(textcheck)


def test_word_counts():
    text = "Ten $50,000 payments in 2033-2042, start-of-year."
    assert textcheck.words_by_spaces(text) == 6
    assert textcheck.words_strict(text) == 9


def test_curly_quotes_are_flagged():
    found = textcheck.non_ascii("Laura’s “floor”")
    assert [ch for _, ch, _ in found] == ["’", "“", "”"]


def test_banned_words_whole_word_only():
    hits = textcheck.banned_hits("Payments are guaranteed; we secured nothing. Unsecured is fine.")
    assert [p for p, _ in hits] == ["guaranteed", "secured"]


def test_first_difference():
    assert textcheck.first_difference("abc", "abc") is None
    assert textcheck.first_difference("Laura's", "Laura’s") == 5
    assert textcheck.first_difference("abc", "abcd") == 3


def test_cli_exit_codes(tmp_path):
    note = tmp_path / "note.txt"
    note.write_text("Growth: one cheap fund.\n")
    paste = tmp_path / "paste.txt"
    paste.write_text("Growth: one cheap fund.")
    assert textcheck.main([str(note), "--limit", "100", "--compare", str(paste)]) == 0
    paste.write_text("Growth: one cheap fund")
    assert textcheck.main([str(note), "--compare", str(paste)]) == 1
    assert textcheck.main([str(note), "--limit", "3"]) == 1
