import argparse
from diversio_stats import get, output

# dashboard_api_path="https://stats.uptimerobot.com/api/getMonitor/Q5ogPt6JAQ?m=785837216"


def uptime_robot(url):
    response = get(url)
    output(response)


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

uptime_robot(args.url)
