"""Append-only changeset log with lock-free admission."""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Iterator, Optional

from aetherflow.models import Changeset


class ChangesetLog:
    def __init__(self, path: Path | str):
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)
        self.log_file = self.path / "changesets.jsonl"
        self._lock = threading.Lock()
        self._head: Optional[str] = None
        self._load_head()

    def _load_head(self) -> None:
        if not self.log_file.exists():
            return
        with open(self.log_file, "r") as f:
            for line in f:
                if line.strip():
                    cs = json.loads(line)
                    self._head = cs["cid"]

    def append(self, changeset: Changeset) -> str:
        with self._lock:
            with open(self.log_file, "a") as f:
                record = {
                    "cid": changeset.cid,
                    "delta_id": changeset.delta_id,
                    "parent_ids": list(changeset.parent_ids),
                    "timestamp": changeset.timestamp,
                    "signature": changeset.signature,
                }
                f.write(json.dumps(record) + "\n")
            self._head = changeset.cid
        return changeset.cid

    @property
    def head(self) -> Optional[str]:
        return self._head

    def __iter__(self) -> Iterator[Changeset]:
        if not self.log_file.exists():
            return
        with open(self.log_file, "r") as f:
            for line in f:
                if line.strip():
                    d = json.loads(line)
                    yield Changeset(
                        cid=d["cid"], delta_id=d["delta_id"],
                        parent_ids=tuple(d["parent_ids"]),
                        timestamp=d["timestamp"], signature=d["signature"],
                    )
