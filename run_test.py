# -*- coding: utf-8 -*-
if __name__ == "__main__":
    import unittest
    import sys

    unittest_args = [
        "--url",
        "https://stats.uptimerobot.com/api/getMonitor/Q5ogPt6JAQ?m=785837216"
    ]
    unittest_args = unittest_args + sys.argv[1:]
    sys.exit(unittest.main(unittest_args))
