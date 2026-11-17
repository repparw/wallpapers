#!/usr/bin/env python3
"""Offline checks for catalog metadata and bundled image checksums."""
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parent.parent
catalog = json.loads((root / "catalog.json").read_text())
assert catalog["schemaVersion"] == 1
items = catalog["wallpapers"]
ids = set()
for item in items:
    identifier = item["id"]
    assert identifier not in ids, f"Duplicate ID: {identifier}"
    ids.add(identifier)
    assert item["category"] in {"atmospheric-sci-fi", "industrial-noir", "cosmic-mystery"}
    assert item["kind"] in {"local", "external"}
    assert item.get("rights")
    if item["kind"] == "local":
        path = Path(item["path"])
        assert not path.is_absolute() and ".." not in path.parts
        data = (root / path).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        assert digest == item["sha256"], f"Hash mismatch: {path}"
        assert "source" not in item
    else:
        assert "path" not in item and "sha256" not in item
        parsed = urlparse(item["source"])
        assert parsed.scheme == "https" and parsed.netloc, identifier
print(f"Validated {len(items)} catalog entries, {sum(x['kind']=='local' for x in items)} bundled images")
