"""The Most Honest Outage Line — a status page message with no spin.

The program writes one line to entry.txt in the output directory: the
status update an AI agent posts while everything is down, saying what
is broken and admitting what it cannot check.
"""

import os

STATUS_LINE = (
    "App, API, and login are down, including the monitoring I would "
    "use to diagnose this. I cannot confirm a cause or an ETA; I'll "
    "post facts as I verify them."
)


def render_status() -> str:
    return STATUS_LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(render_status())


if __name__ == "__main__":
    main()
