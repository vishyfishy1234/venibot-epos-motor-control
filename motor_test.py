import argparse
from epos_interface import Epos
from mock_epos import MockEpos


def print_status(status):
    print("\n--- STATUS ---")
    for k, v in status.items():
        print(f"{k}: {v}")
    print("--------------")


def run(epos, mock=False):
    epos.open()
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
                epos.disable()
                epos.close()
                break
            else:
                print("Unknown command.")
        except Exception as exc:
            print(f"ERROR: {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock", action="store_true")
    args = parser.parse_args()

    if args.mock:
        run(MockEpos(), mock=True)
    else:
        epos = Epos()
        try:
            run(epos)
        finally:
            epos.close()
