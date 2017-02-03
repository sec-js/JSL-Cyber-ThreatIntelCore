#!/usr/bin/env python


from __future__ import print_function

try:
    import sys
    import argparse
    from config.stats import Stats
    from lib.core.search import Search
    from lib.migration.mongo import Migrate
    from config.constants import build, title
    from lib.common.utils import enum_classes, mongo_server
except ImportError as e:
    print("[!] Missing a dependency:", str(e))
    sys.exit()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", metavar=('method', 'CVE'), help="Invoking multiple vFeed built-in functions",
                        nargs=2)
    parser.add_argument("-e", "--export", metavar=('json_dump', 'CVE'), help="Export the JSON content", nargs=2)
    parser.add_argument("-s", "--search", metavar=('cve|cpe|cwe|oval|text', 'entry'),
                        help="Search for CVE,CPE,CWE, OVAL or free text",
                        nargs=2)
    parser.add_argument("-u", "--update", help="Update the database", action="store_true", required=False)
    parser.add_argument("--stats", metavar="get_stats | get_latest", type=str,
                        help="View the vFeed Database statistics", nargs=1)
    parser.add_argument("--list", help="Enumerate the list of available built-in functions", action="store_true",
                        required=False)
    parser.add_argument("--migrate", help="Migration to MongoDB", action="store_true", required=False)

    args = parser.parse_args()

    if args.search:
        method = args.search[0]
        cve_id = args.search[1]
        try:
            result = getattr(Search(cve_id), method)
            print(result())
        except Exception as e:
            print("[!] Unknown built-in function:", str(e))

    if args.update:
        print("[+]  Database must be downloaded")
        print("[+] Once downloaded, decompress it into your API repository.")



    if args.migrate:
        # checking whether the MongoDB server is running
        if mongo_server("mongod"):
            print("[+] Mongo service is up. Starting migrating ....")
            Migrate()
        else:
            print("[!] Mongo service is probably not up.")

    if args.stats:
        method_name = args.stats[0]
        try:
            result = getattr(Stats(), method_name)
            print(result())
        except Exception as e:
            print("[!] Unknown built-in function:", str(e))

    if args.list:
        enum_classes("list", "")

    if args.method:
        method_name = args.method[0]
        cve_id = args.method[1]
        result = enum_classes(method_name, cve_id)
        print(result)

    if args.export:
        method_name = args.export[0]
        cve_id = args.export[1]
        result = enum_classes(method_name, cve_id)
        if result is not False:
            print(result)
