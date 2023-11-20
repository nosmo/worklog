#!/usr/bin/env python3

import argparse
import datetime
import fileinput
import os
import sys

import yaml

WORKLOG_F = "~/.worklog.yaml"

def main():

    msg = "Work logging script"
    parser = argparse.ArgumentParser(description=msg,
                                     epilog='Worklog entry can be provided via stdin or commandline')

    parser.add_argument(nargs="?",
                        dest="log_msg",
                        help="message to be added to worklog")

    parser.add_argument("--tee",
                        action="store_true",
                        required=False,
                        help="tee-like: print input from stdin")


    parser.add_argument('-T', '--tag',
                        action="append",
                        default=[],
                        help="Tags to associate with this entry")

    args = parser.parse_args()

    message = args.log_msg
    if not args.log_msg:
        message = sys.stdin.read()
        if args.tee:
            print(message)

    worklog_path = os.path.expanduser(WORKLOG_F)

    if os.path.exists(worklog_path):
        with open(worklog_path) as worklog_f:
            current_log = yaml.safe_load(worklog_f)
            #todo check for rotation/backup
            #TODO always create a .new
    else:
        #todo log
        #todo confirm creating new blank log
        input_str = input("Worklog appears to be empty - please type y to create a new one\n")
        if input_str.strip() != "y":
            print("Not creating new worklog - exiting")
            return 1

        current_log = {}

    now = datetime.datetime.now()
    ymd = "{}-{}-{}".format(now.year, now.month, now.day)
    today_log = current_log.setdefault(ymd, {})
    time_str = "{:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second)
    current_log[ymd][time_str] = {"entry": message,
                                  "tags": args.tag}

    with open(os.path.expanduser(worklog_path), "w") as worklog_f:
        yaml.dump(current_log, stream=worklog_f)

    print("Logged message at {:02d}:{:02d}:{:02d}".format(now.hour, now.minute, now.second))

    return 0

if __name__ == "__main__":
    sys.exit(main())
