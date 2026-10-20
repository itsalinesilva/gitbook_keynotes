import json
import logging
logger = logging.getLogger("brain_os.audit")
def emit_event(event, **fields):
    logger.info(json.dumps({"event": event, **fields}, ensure_ascii=False, sort_keys=True))
