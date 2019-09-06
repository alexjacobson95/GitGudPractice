from engine import text_engine

def test_popup():
    assert text_engine.display_popup(" ") is None
