import json
import subprocess

import click


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


def restart_server():
    click.echo("\nRestart v2ray service...")
    subprocess.call("systemctl restart v2ray.service", shell=True)
    click.echo("Done...\n")
