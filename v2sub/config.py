from v2sub import utils

V2RAY_CONFIG_FILE = "/etc/v2ray/config.json"


def _get_config(addr: str, port: int, id_: str, client_port=1080) -> dict:
    return {
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


def update_config(node: dict, client_port: int):
    v2ray_config = _get_config(node['add'], int(node['port']), node['id'],
                               client_port=client_port)
    utils.write_to_json(v2ray_config, V2RAY_CONFIG_FILE)
