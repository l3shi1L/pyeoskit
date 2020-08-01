import os
import sys
import time
import pytest
import logging
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from pyeoskit.chainapi import ChainApi

@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

class Test(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    async def api_test(self):
        logger.info('hello,world')
        api = ChainApi('UUOS', 'http://127.0.0.1:8888', True)
        r = await api.get_info()
        logger.info(r)
        r = await api.get_account('eosio')
        logger.info(r)

    def test_basic(self, event_loop):
        event_loop.run_until_complete(self.api_test())
