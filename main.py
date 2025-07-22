import argparse
from ggit.init import git_init
from ggit.hash_object import hash_object

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    subparsers.add_parser("init")

    # hash-object
    hash_parser = subparsers.add_parser("hash-object")
    hash_parser.add_argument("path")

    args = parser.parse_args()

    sif args.command == "init":
        git_init()
    elif args.command == "hash-object":
        hash_object(args.path)
    else:
        print(f"Unknown command {args.command}")
    
if __name__ == "__main__":
    main()
