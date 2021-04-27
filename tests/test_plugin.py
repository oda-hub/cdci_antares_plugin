import subprocess
import requests
import time
import re
import json
import signal
import os
import random
import traceback
import logging
import jwt

from threading import Thread
from time import sleep

import pytest


logger = logging.getLogger(__name__)

default_params = dict(
                    query_status="new",
                    query_type="Real",
                    instrument="antares",
                    product_type="antares_spectrum",
                    T1="2008-03-19T06:11:11.0",
                    T2="2008-03-19T06:12:11.0",
                    async_dispatcher=False,
                 )

def test_discover_plugin():
    import cdci_data_analysis.plugins.importer as importer

    assert 'dispatcher_plugin_antares' in  importer.cdci_plugins_dict.keys()

    
def test_(dispatcher_live_fixture):
    server = dispatcher_live_fixture

    logger.info("constructed server: %s", server)
    c = requests.get(server + "/run_analysis",
                     params = default_params)

    logger.info("content: %s", c.text)
    jdata = c.json()
    logger.info(json.dumps(jdata, indent=4, sort_keys=True))
    logger.info(jdata)
    assert c.status_code == 200

    assert jdata['job_status'] == 'done'
    
