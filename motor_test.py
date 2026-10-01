import argparse

from epos_interface import Epos
from mock_epos import MockEpos


def print_status(status):
    print("\n--- STATUS ---")
    for k, v in status.items():
        print(f"{k}: {v}")
    print("--------------")


def run(epos):
    epos.open()
    try:
        print("Connected.")
        print_status(epos.status())

        print("\nCommands: i=status, e=enable, d=disable, c=clear fault, q=quit")
        while True:
            cmd = input("> ").strip().lower()
            try:
                if cmd == "i":
                    print_status(epos.status())
                elif cmd == "e":
                    epos.enable()
                elif cmd == "d":
                    epos.disable()
                elif cmd == "c":
                    epos.clear_fault()
                elif cmd == "q":
                    break
                else:
                    print("Unknown command.")
            except RuntimeError as exc:
                print(f"ERROR: {exc}")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
    finally:
        try:
            epos.disable()
        except RuntimeError as exc:
            print(f"ERROR: disable failed: {exc}")
        epos.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock", action="store_true")
    args = parser.parse_args()

    run(MockEpos() if args.mock else Epos())
