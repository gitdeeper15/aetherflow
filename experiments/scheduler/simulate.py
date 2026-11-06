"""Compare adaptive scheduling vs FIFO."""

import json
from pathlib import Path

from aetherflow import Changeset, AdaptiveScheduler


def simulate(n_jobs: int = 1000) -> dict:
    jobs = [
        Changeset(f"c{i}", f"d{i}", (f"c{i-1}",) if i > 0 else (), float(i), f"c{i}")
        for i in range(n_jobs)
    ]

    # FIFO: process in arrival order
    fifo_order = [j.cid for j in jobs]

    # Adaptive: schedule by priority
    scheduler = AdaptiveScheduler()
    for i, job in enumerate(jobs):
        recent = jobs[max(0, i-10):i]
        scheduler.schedule(job, recent=recent, out_degree=(n_jobs - i) % 10)

    adaptive_order = []
    while len(scheduler) > 0:
        adaptive_order.append(scheduler.next().cid)

    # Measure: how many jobs are "urgent" (out_degree > 5) and where they appear
    urgent = {f"c{i}" for i in range(n_jobs) if (n_jobs - i) % 10 > 5}

    fifo_urgent_pos = [i for i, cid in enumerate(fifo_order) if cid in urgent]
    adaptive_urgent_pos = [i for i, cid in enumerate(adaptive_order) if cid in urgent]

    return {
        "n_jobs": n_jobs,
        "fifo_mean_urgent_position": sum(fifo_urgent_pos) / len(fifo_urgent_pos) if fifo_urgent_pos else 0,
        "adaptive_mean_urgent_position": sum(adaptive_urgent_pos) / len(adaptive_urgent_pos) if adaptive_urgent_pos else 0,
        "n_urgent": len(urgent),
    }


if __name__ == "__main__":
    result = simulate()
    print(f"Jobs: {result['n_jobs']}, Urgent: {result['n_urgent']}")
    print(f"FIFO mean urgent position:     {result['fifo_mean_urgent_position']:.1f}")
    print(f"Adaptive mean urgent position: {result['adaptive_mean_urgent_position']:.1f}")

    out = Path(__file__).parent / "results.json"
    out.write_text(json.dumps(result, indent=2))
    print(f"✅ Results saved to {out}")
