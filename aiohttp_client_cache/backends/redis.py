from .base import BaseCache
from .storage.redisdict import RedisDict


class RedisCache(BaseCache):
    """Redis cache backend"""

    def __init__(self, namespace='requests-cache', **options):
        """
        :param namespace: redis namespace (default: ``'requests-cache'``)
        :param connection: (optional) ``redis.StrictRedis``
        """
        super().__init__(**options)
        self.responses = RedisDict(namespace, 'responses', options.get('connection'))
        self.keys_map = RedisDict(namespace, 'urls', self.responses.connection)