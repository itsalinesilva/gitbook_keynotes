import sqlite3, json
from pathlib import Path

class BrainStore:
    """Local SQLite store for source registry, documents and reviewable memory proposals."""
    def __init__(self, path="data/brain_os.sqlite3"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as con:
            con.executescript("""
            CREATE TABLE IF NOT EXISTS sources (
              source_id TEXT PRIMARY KEY, canonical_url TEXT NOT NULL, title TEXT NOT NULL,
              source_type TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'unverified',
              metadata_json TEXT NOT NULL DEFAULT '{}');
            CREATE TABLE IF NOT EXISTS documents (
              document_id TEXT PRIMARY KEY, source_id TEXT, title TEXT NOT NULL,
              body TEXT NOT NULL, content_hash TEXT NOT NULL, created_at TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS memory_proposals (
              proposal_id TEXT PRIMARY KEY, content TEXT NOT NULL, evidence_json TEXT NOT NULL,
              status TEXT NOT NULL DEFAULT 'proposed', created_at TEXT NOT NULL, reviewed_by TEXT);
            CREATE INDEX IF NOT EXISTS idx_documents_source ON documents(source_id);
            """)
    def _connect(self):
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row
        return con
    def add_source(self, source_id, url, title, source_type, status="unverified", metadata=None):
        with self._connect() as con:
            con.execute("INSERT INTO sources VALUES (?,?,?,?,?,?)",
                (source_id, url, title, source_type, status, json.dumps(metadata or {})))
    def list_sources(self):
        with self._connect() as con:
            return [dict(r) for r in con.execute("SELECT * FROM sources ORDER BY title")]
    def add_document(self, document_id, source_id, title, body, content_hash, created_at):
        with self._connect() as con:
            con.execute("INSERT INTO documents VALUES (?,?,?,?,?,?)",
                (document_id, source_id, title, body, content_hash, created_at))
    def search_documents(self, query):
        pattern = f"%{query}%"
        with self._connect() as con:
            rows = con.execute("SELECT * FROM documents WHERE title LIKE ? OR body LIKE ? LIMIT 20",
                                (pattern, pattern)).fetchall()
            return [dict(r) for r in rows]
    def propose_memory(self, proposal_id, content, evidence, created_at):
        with self._connect() as con:
            con.execute("INSERT INTO memory_proposals "
                "(proposal_id,content,evidence_json,status,created_at) VALUES (?,?,?,'proposed',?)",
                (proposal_id, content, json.dumps(evidence), created_at))
    def review_memory(self, proposal_id, reviewer, approve):
        with self._connect() as con:
            cur = con.execute("UPDATE memory_proposals SET status=?,reviewed_by=? "
                "WHERE proposal_id=? AND status='proposed'",
                ("approved" if approve else "rejected", reviewer, proposal_id))
            if cur.rowcount != 1:
                raise ValueError("proposal not found or already reviewed")
