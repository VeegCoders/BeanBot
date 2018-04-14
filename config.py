LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class':        'logging.StreamHandler',
            'formatter':    'default',
            'level':        'DEBUG',
        },
        'file': {
            'class':        'logging.handlers.RotatingFileHandler',
            'formatter':    'default',
            'level':        'INFO',
            'filename':     'log/beanbot.log',
            'maxBytes':     1024,
            'backupCount':  3
        },
    },
    'loggers': {
        'root': {
            'level':    'DEBUG'
        },
        'BeanBot': {
            'level':    'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'BeanBot-db': {
            'level':    'DEBUG',
            'handlers': ['console', 'file'],
            'propagate':  True,
        },
        'BeanBot-points': {
            'level':    'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': True,
        }
    }
}