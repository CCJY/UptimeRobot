import sys
import argparse
from diversio.uptime_robot_client import UptimeRobotClient

# dashboard_api_path="https://stats.uptimerobot.com/api/getMonitor/Q5ogPt6JAQ?m=785837216"


def get_parser():
    parser = argparse.ArgumentParser(
        prog="find_uptime_highest_ping", usage="%(prog)s <url>")
    parser.add_argument('--url', dest="url", help="URL to work with")
    return parser


parser = get_parser()
args = parser.parse_args()

if not args.url:
    print(parser.print_help())
    sys.exit(2)

robot = UptimeRobotClient()

robot.run(args.url)
