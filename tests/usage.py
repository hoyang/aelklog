#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ezlogging

def test_log():
    logger = ezlogging.setup_logstash_logger(logger_name="download", logstash_host="192.168.77.8", logstash_port=5045)
    
    logger.debug("This is a debug message", extra={"user": "alice", "action": "test_debug"})
    logger.info("This is an info message", extra={"user": "bob", "action": "test_info"})
    logger.warning("This is a warning message", extra={"user": "carol", "action": "test_warning"})
    logger.error("This is an error message", extra={"user": "dave", "action": "test_error"})
    logger.critical("This is a critical message", extra={"user": "eve", "action": "test_critical"})

    print("Logs have been sent. Please check your Logstash/ELK stack.")
