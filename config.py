server_ip = '127.0.0.1'
server_tcp = 9090
init_tcp = 9091
resp_tcp = 9092

logging_conf = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'server.log',
            'mode': 'a',
            'formatter': 'detailed',
        },
    },
    'loggers': {
        'idl_service': {
            'level': 'DEBUG',
            'handlers': ['file']
        },
        'terminal': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'async_response_server': {
            'level': 'DEBUG',
            'handlers': ['console']
        },
        'async_initial_server': {
            'level': 'DEBUG',
            'handlers': ['console']
        }

    }
}
