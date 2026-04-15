"""
Deflect One CLI entry point.

This thin wrapper imports and calls main() from the bundled deflect.py
so that the 'deflect' and 'deflect-one' console scripts work after
`pip install deflect-one`.

Usage after install:
    deflect              # real SSH mode
    deflect --demo       # demo mode, no SSH needed
    deflect-one --demo   # same, alternative command name
"""

import importlib.util
import sys
from pathlib import Path


def main() -> None:
    """
    Locate deflect.py inside the installed package and call its main().

    deflect.py lives next to this file in the installed package directory:
        <site-packages>/deflect_one/deflect.py
    """
    here    = Path(__file__).parent
    script  = here / "deflect.py"

    if not script.exists():
        print(
            f"[deflect-one] ERROR: deflect.py not found at {script}\n"
            "The package installation may be incomplete. Try:\n"
            "    pip install --force-reinstall deflect-one",
            file=sys.stderr,
        )
        sys.exit(1)

    spec   = importlib.util.spec_from_file_location("deflect", script)
    module = importlib.util.module_from_spec(spec)          # type: ignore[arg-type]

    # Register under its natural name so internal imports work correctly
    sys.modules["deflect"] = module
    spec.loader.exec_module(module)                          # type: ignore[union-attr]

    module.main()


if __name__ == "__main__":
    main()
