from v2sub import utils

V2RAY_CONFIG_FILE = "/etc/v2ray/config.json"


def _update_config(addr, id_, port, client_port=1080):
    v2ray_config = {
        "inbounds": [
            {
                "port": client_port,
                "listen": "127.0.0.1",
                "protocol": "socks",
                "sniffing": {
                    "enable": True,
                    "destOverride": ["http", "tls"]
                },
                "settings": {
                    "auth": "noauth",
                    "udp": True
                }
            }
        ],
        "outbounds": [
            {
                "protocol": "vmess",
                "settings": {
                    "vnext": [
                        {
                            "address": addr,
                            "port": port,
                            "users": [{"id": id_}]
                        }
                    ]
                }
            },
            {
                "protocol": "freedom",
                "tag": "direct",
                "settings": {}
            }
        ],
        "routing": {
            "domainStrategy": "IPOnDemand",
            "rules": [
                {
                    "type": "field",
                    "domain": ["geosite:cn"],
                    "ip": ["geoip:private", "geoip:cn"],
                    "outboundTag": "direct"
                }
            ]
        }
    }
    utils.write_to_json(v2ray_config, V2RAY_CONFIG_FILE)


def update_config(node: dict, client_port: int):
    addr = node['add']
    id_ = node['id']
    port = int(node['port'])
    _update_config(addr, id_, port, client_port)
