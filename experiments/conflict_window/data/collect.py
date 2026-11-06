"""Collect (τ, O, conflict) triples from a real Git repository."""

import json
import subprocess
from pathlib import Path


def collect(repo_path: Path, max_pairs: int = 5000) -> list[dict]:
    result = subprocess.run(
        ["git", "-C", str(repo_path), "log", "--pretty=format:%H|%at", "-n", "500"],
        capture_output=True, text=True, check=True,
    )
    commits = []
    for line in result.stdout.strip().split("\n"):
        if "|" in line:
            sha, ts = line.split("|")
            files = subprocess.run(
                ["git", "-C", str(repo_path), "show", "--name-only", "--pretty=format:", sha],
                capture_output=True, text=True,
            ).stdout.strip().split("\n")
            commits.append({
                "sha": sha,
                "timestamp": int(ts),
                "files": set(f for f in files if f),
            })

    pairs = []
    for i in range(len(commits)):
        for j in range(i + 1, min(i + 30, len(commits))):
            a, b = commits[i], commits[j]
            tau = abs(a["timestamp"] - b["timestamp"]) / 3600.0
            if not a["files"] or not b["files"]:
                continue
            overlap = len(a["files"] & b["files"]) / len(a["files"] | b["files"])
            if overlap > 0:
                pairs.append({"tau": tau, "overlap": overlap, "conflict": 0})
            if len(pairs) >= max_pairs:
                break
        if len(pairs) >= max_pairs:
            break

    return pairs


if __name__ == "__main__":
    repo = Path(__file__).parent / "repo"
    if not repo.exists():
        print(f"⚠️  Clone a repository into {repo} first:")
        print(f"    git clone --depth 500 https://github.com/git/git.git {repo}")
        raise SystemExit(1)

    pairs = collect(repo)
    out = Path(__file__).parent / "pairs.json"
    out.write_text(json.dumps(pairs, indent=2))
    print(f"✅ Collected {len(pairs)} pairs → {out}")
