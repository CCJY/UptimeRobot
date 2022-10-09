import urllib.request
import re


def get_extract_from_html(url, extract_var) -> str:
    try:
        urlf = urllib.request.urlopen(url)
        html = urlf.read().decode('utf-8')

        extract_value = re.search(
            'var {0} = (.+?);'.format(extract_var), html).group(1).strip("'")

        return extract_value

    except urllib.error.URLError as err:
        raise err
    except Exception as err:
        raise err
