# v2sub

一个用`python3`写的`v2ray`订阅器

* [English version](./README.md)

功能:

- 支持多个订阅

- 直接运行系统`v2ray`命令，好处是可以通过`systemctl`控制

- 支持节点延迟测试

## 安装

```bash
pip install v2sub
```

或者

```bash
pip install git+https://github.com/airborne007/v2sub.git@master
```

## 使用

**注意：** 使用之前，我假定你系统上已经安装好了`v2ray`和`v2sub`

如果你只有一个订阅源，那么使用就非常简单了。按照以下步骤操作（需要root或者sudo）：

1. 添加一个订阅源

    ```bash
    v2sub add [url]
   ```

2. 更新订阅

    ```bash
    v2sub update
   ```

3. 运行

    ```bash
    v2sub run [index]
   ```
   
   *更新订阅后会列出所有节点，`index`就是节点序号*

## 更详细说明

1. 帮助信息

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

2. 添加或更新订阅

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

3. 更新订阅

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

4. 列出订阅下的节点

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

5. 移除订阅及其节点

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

6. 运行或切换节点运行

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

7. 节点延迟测试

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

支持更多功能.

## 其它

理论上这个程序可以运行在所有 linux 平台， 但是我只在`Arch Linux`上面做了测试。 如果你在
其它 linux 发行版上面使用时遇到任何问题，欢迎提交 Issue 或者 PR 。