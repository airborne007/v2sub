#!/usr/bin/env python
import click
from simple_term_menu import TerminalMenu

from v2sub import DEFAULT_SUBSCRIBE
from v2sub import __version__
from v2sub import config
from v2sub import subscribe
from v2sub.systemd import *
from v2sub import utils


@click.group()
def cli():
    """A v2ray subscriber written in python3"""
    subscribe.init()


@cli.command()
def version():
    """show version"""
    click.echo(__version__)


@cli.command()
@click.argument("url")
@click.option("--name", default=DEFAULT_SUBSCRIBE,
              help="name of the subscribe, if not provided, a default name "
                   "will be given.")
def add(url, name):
    """add a subscribe.

    URL: url of the subscribe
    """
    subscribe.add_subscribe(url, name)


@cli.command()
@click.option("--name", default=DEFAULT_SUBSCRIBE,
              help="name of subscribe will be removed, if not provided, "
                   "default subscribe will be removed.")
@click.option("--all-subs", "--all", is_flag=True, default=False,
              help="whether remove all subscribe, default is False.")
def remove(name, all_subs):
    """remove subscribe and it's nodes."""
    subscribe.remove_subscribe(name, all_subs=all_subs)


@cli.command()
@click.option("--name", default=DEFAULT_SUBSCRIBE,
              help="the name of the subscribe you want to update, if not "
                   "provided, default subscribe will be updated.")
@click.option("--all-subs", "--all", is_flag=True, default=False,
              help="whether to update all subscribe, default is False.")
def update(name, all_subs):
    """update subscribe nodes."""
    subscribe.update_subscribe(name=name, all_subs=all_subs)


@cli.command(name="list")
@click.option("--name",
              default=DEFAULT_SUBSCRIBE,
              help="the name of the subscribe you want list, if not provided, "
                   "default subscribe will be listed.")
@click.option("--all-subs", "--all", is_flag=True, default=False,
              help="whether list all subscribe, default is False.")
def list_servers(name, all_subs):
    """list subscribe nodes."""
    subscribe.list_servers(name, all_subs=all_subs)


@cli.command()
@click.option("--name", default=DEFAULT_SUBSCRIBE,
              help="the name of the subscribe you want ping with. if not "
                   "provided, default subscribe will be pinged.")
@click.option("--index", type=click.INT,
              help="the node of subscribe you want to ping with. if not "
                   "provided, will test all node delay.")
def ping(name, index):
    """test node delay by ping."""
    utils.ping(name=name, index=index)


@cli.command()
@click.option("--name", default=DEFAULT_SUBSCRIBE,
              help="the name of the subscribe you want run with. if not "
                   "provided, the default subscribe will be run.")
@click.option("--port", type=click.INT, default=1080,
              help="the local port v2ray client listen on, default is 1080")
def run(name, port):
    """start v2ray with a selected node.
    """
    servers = subscribe.get_servers(name)
    menu = TerminalMenu(servers, title=name)
    index = menu.show()
    node = subscribe.get_node(index, name)
    existing_unit = utils.read_from_json(systemd.SYSTEMD_UNIT).get("unit", "")
    existing_config = utils.read_from_json(config.V2RAY_CONFIG_FILE)
    if existing_config != node:
        systemd.stop(existing_unit)
        config.update_config(node, port)
    if not systemd.is_active(existing_unit):
        unit = systemd.start(["v2ray", "-config", config.V2RAY_CONFIG_FILE])
        utils.write_to_json(unit, systemd.SYSTEMD_UNIT)


@cli.command()
def stop():
    """stop v2ray
    """
    unit = utils.read_from_json(systemd.SYSTEMD_UNIT).get("unit", "")
    if systemd.is_active(unit):
        systemd.stop(unit)
    click.echo("Stopped")


if __name__ == '__main__':
    cli()
