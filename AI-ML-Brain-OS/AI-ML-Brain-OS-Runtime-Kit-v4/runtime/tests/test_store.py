from brain_os.store import BrainStore
def test_source_and_memory(tmp_path):
    store = BrainStore(str(tmp_path / "brain.sqlite3"))
    store.add_source("s1","https://example.org","Example","other")
    assert store.list_sources()[0]["source_id"] == "s1"
    store.propose_memory("m1","candidate",["e1"],"2026-10-19T00:00:00Z")
    store.review_memory("m1","reviewer",True)
