# v2sub

A v2ray subscriber written by python3

## Simple Usage

If you only have one subscribe, just do as following steps (root or sudo is needed).

1. install `v2ray` first if you don't have installed

2. install `v2sub`

    ```bash
    pip install git+https://github.com/airborne007/v2sub.git@master
    ```

3. add a subscribe

    ```bash
    v2sub add [url]
    ```

4. update subscribe
    
    ```bash
    v2sub update
    ```
5. run and enjoin it

    ```bash
    v2sub run [index]
    ```


## Features

- multiple subscribes support

- run system `v2ray` which you can be controlled by `systemctl` command

- node delay test is support by `ping`

## More details

1. help message

    ```bash
    # v2sub --help
    Usage: v2sub [OPTIONS] COMMAND [ARGS]...
    
      A v2ray subscriber written by python3
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      add      add a subscribe.
      list     list subscribe nodes.
      ping     test node delay by ping.
      remove   remove subscribe.
      run      start v2ray with an specify node.
      update   update subscribe nodes.
      version  show version
    ```
2. add or update subscribe
    
    ```bash
    # v2sub add --help
    Usage: v2sub add [OPTIONS] URL
    
      add a subscribe.
    
      URL: url of the subscribe
    
    Options:
      --name TEXT  name of the subscribe, if not provided, a default name will be
                   given.
      --help       Show this message and exit.
    ```

3. update subscribe nodes

    ```bash
    # v2sub update --help
    Usage: v2sub update [OPTIONS]
    
      update subscribe nodes.
    
    Options:
      --name TEXT        the name of the subscribe you want to update, if not
                         provided, default subscribe will be updated.
      --all-subs, --all  whether to update all subscribe, default is False.
      --help             Show this message and exit.
    ```

4. list subscribe nodes

    ```bash
    # v2sub list --help
    Usage: v2sub list [OPTIONS]
    
      list subscribe nodes.
    
    Options:
      --name TEXT        the name of the subscribe you want list, if not provided,
                         default subscribe will be listed.
      --all-subs, --all  whether list all subscribe, default is False.
      --help             Show this message and exit.
    ```

5. remove subscribe and it's nodes

    ```bash
    # v2sub remove --help
    Usage: v2sub remove [OPTIONS]
    
      remove subscribe and it\'s nodes.
    
    Options:
      --name TEXT        name of subscribe will be removed, if not provided,
                         default subscribe will be removed.
      --all-subs, --all  whether remove all subscribe, default is False.
      --help             Show this message and exit.
    ```

6. run or switch `v2ray` service

    ```bash
    # v2sub run --help
    Usage: v2sub run [OPTIONS] INDEX
    
      start v2ray with an specify node.
    
      INDEX: the index node id list before.
    
    Options:
      --name TEXT     the name of the subscribe you want run with. if not
                      provided, the default subscribe will be run.
      --port INTEGER  the local port v2ray client listen on, default is 1080
      --help          Show this message and exit.
    ```
7. test node delay

    ```bash
    Usage: v2sub ping [OPTIONS]
    
    Options:
      --name TEXT      the name of the subscribe you want ping with. if not
                       provided, default subscribe will be pinged.
      --index INTEGER  the node of subscribe you want to ping with. if not
                       provided, will test all node delay.
      --help           Show this message and exit.
    ```
   
## TODO

support more features.

## More

This program can run on all Linux platforms in theory, but I only tested it on
`Arch Linux`. If you have any problems with other linux distributions, issue or
pull request is welcome.