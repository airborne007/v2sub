import json
import re
import sys
from subprocess import call, Popen, PIPE

import click

from v2sub import subscribe


def write_to_json(obj, filename):
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=2)


def read_as_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (IOError, json.decoder.JSONDecodeError):
        return {}


def str2byte(string: str) -> bytes:
    return string.encode('utf-8')


def byte2str(byte: bytes) -> str:
    return byte.decode('utf-8')


def check_index(index: int):
    if index - 1 < 0:
        raise IndexError("node index should be positive.")


def echo_node(index, node, delay=None):
    s = '[' + str(index) + ']' + node['ps']
    if delay:
        s += "--timeout" if delay == -1 else "--%sms" % str(delay)
    else:
        s += "--%s" % node['add']
    click.echo(s)


def restart_server():
    click.echo("restart v2ray service...")
    call("systemctl restart v2ray.service", shell=True)
    click.echo("Done...")


def _ping(ip, times=3, timeout=1, interval=0.2):
    times, timeout, interval = str(times), str(timeout), str(interval)
    cmd = ['ping', '-n', '-W', timeout, '-c', times, "-i", interval, ip]
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, _ = proc.communicate()
    reg = r'min/avg/max/mdev = ([0-9]+.[0-9]+)/([0-9]+.[0-9]+)'
    s = re.search(reg, str(output))
    if s:
        return s.group(2)
    return -1


def ping(name=subscribe.DEFAULT_SUBSCRIBE, index=None, all_servers=None):
    if all_servers is None:
        all_servers = read_as_json(subscribe.SERVER_CONFIG)
    try:
        servers = all_servers[name]
    except KeyError:
        click.echo("Unknown subscribe: %s, please check it." % name)
        sys.exit(1)
    if index is not None:
        try:
            check_index(index)
            node = servers[index - 1]
        except IndexError:
            click.echo("Invalid index: %s, please check it." % index)
            sys.exit(1)
        delay = _ping(node['add'])
        echo_node(index, node, delay=delay)
    else:
        for index, node in enumerate(servers, start=1):
            delay = _ping(node['add'])
            echo_node(index, node, delay=delay)
