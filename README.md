# aelklog

###  A simple logging package that sends logs asynchronously to ELK with customizable fields. 

### Usage
```python
import aelklog

log4km = aelklog.setup_logstash_logger(logger_name="raster_image_4km", logstash_host="192.168.77.8", logstash_port=5045)
log16km = aelklog.setup_logstash_logger(logger_name="raster_image_16km", logstash_host="192.168.77.8", logstash_port=5045)

def test4km():
    log4km.warning("test", extra={"custom_fields": {"who": "you"}})

def test16km():
    log16km.warning("test", extra={"custom_fields": {"who": "fangj"}})

if __name__ == '__main__':
    test4km()
    test16km()
```
