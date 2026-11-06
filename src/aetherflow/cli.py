"""Command-line interface for AetherFlow v2.0.0."""

import argparse
import sys

from aetherflow.__version__ import __version__
from aetherflow.conflict.window import conflict_window
from aetherflow.remediation.bound import remediation_bound, minimum_tier_depth


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="aetherflow", description="AetherFlow v2.0.0")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    cw = sub.add_parser("conflict-window")
    cw.add_argument("--tau", type=float, required=True)
    cw.add_argument("--overlap", type=float, required=True)
    cw.add_argument("--kappa", type=float, default=3.0)
    cw.add_argument("--theta", type=float, default=4.0)

    rb = sub.add_parser("remediation-bound")
    rb.add_argument("--lambda-fail", type=float, required=True)
    rb.add_argument("--mu-remediate", type=float, required=True)
    rb.add_argument("--K", type=int, required=True)
    rb.add_argument("--gamma", type=float, default=0.15)
    rb.add_argument("--T-react", type=float, default=8.0)

    mt = sub.add_parser("min-tier-depth")
    mt.add_argument("--epsilon", type=float, required=True)
    mt.add_argument("--rho", type=float, required=True)
    mt.add_argument("--gamma", type=float, default=0.15)
    mt.add_argument("--T-react", type=float, default=8.0)

    args = parser.parse_args(argv)

    if args.command == "conflict-window":
        print(f"W = {conflict_window(args.tau, args.overlap, args.kappa, args.theta):.6f}")
    elif args.command == "remediation-bound":
        print(f"P(Remediation) ≥ {remediation_bound(args.lambda_fail, args.mu_remediate, args.K, args.gamma, args.T_react):.6f}")
    elif args.command == "min-tier-depth":
        print(f"K ≥ {minimum_tier_depth(args.epsilon, args.rho, args.gamma, args.T_react)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
