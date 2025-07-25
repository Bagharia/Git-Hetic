import argparse
from ggit.init import git_init
from ggit.hash_object import hash_object
from ggit.add import git_add
from ggit.write_tree import write_tree
from ggit.commit import it_commit
from ggit.ls_files import git_ls_files
from ggit.commit_tree import commit_tree
from ggit.show_ref import git_show_ref
from ggit.log import git_log
from ggit.ls_tree import git_ls_tree
from ggit.rev_parse import git_rev_parse
from ggit.status import git_status
from ggit.checkout import git_checkout

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    subparsers.add_parser("init")

    # hash-object
    hash_parser = subparsers.add_parser("hash-object")
    hash_parser.add_argument("path")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("path")

    # write-tree
    subparsers.add_parser("write-tree")

    # commit-tree
    commit_parser = subparsers.add_parser("commit-tree")
    commit_parser.add_argument("tree_sha")
    commit_parser.add_argument("-m", "--message", required=True)
    commit_parser.add_argument("-p", "--parent")

    # commit  
    commit_porcelain = subparsers.add_parser("commit")
    commit_porcelain.add_argument("-m", "--message", required=True)

    # ls-files
    subparsers.add_parser("ls-files")
    
    # show-ref
    subparsers.add_parser("show-ref")

    # log
    subparsers.add_parser("log")
    
    # ls-tree
    ls_tree_parser = subparsers.add_parser("ls-tree")
    ls_tree_parser.add_argument("tree_sha")

    # rev-parse
    rev_parse_parser = subparsers.add_parser("rev-parse")
    rev_parse_parser.add_argument("ref")
    
    # status
    subparsers.add_parser("status")
    
    # checkout
    checkout_parser = subparsers.add_parser("checkout")
    checkout_parser.add_argument("commit_ref")

    args = parser.parse_args()

    if args.command == "init":
        git_init()
    elif args.command == "hash-object":
        hash_object(args.path)
    elif args.command == "add":
        git_add(args.path)
    elif args.command == "write-tree":
        write_tree()
    elif args.command == "commit-tree":
        commit_tree(args.tree_sha, args.message, args.parent)
    elif args.command == "commit":
        it_commit(args.message)
    elif args.command == "ls-files":
        git_ls_files()
    elif args.command == "show-ref":
        git_show_ref()
    elif args.command == "log":
        git_log()
    elif args.command == "ls-tree":
        git_ls_tree(args.tree_sha)
    elif args.command == "rev-parse":
        git_rev_parse(args.ref)
    elif args.command == "status":
        git_status()
    elif args.command == "checkout":
        git_checkout(args.commit_ref)
    else:
        print(f"Unknown command {args.command}")
    
if __name__ == "__main__":
    main()
