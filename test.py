import logging.handlers

import platform
import os

def is_raspberry_pi():
    """Return True if running on a Raspberry Pi with Raspbian OS"""
    try:
        # Check if "Raspberry Pi" in hardware info
        if os.path.exists("/proc/device-tree/model"):
            with open("/proc/device-tree/model", "r") as f:
                model = f.read().lower()
                if "raspberry pi" in model:
                    return True

        # Fallback: check distribution
        try:
            import distro
            if "raspbian" in distro.id().lower() or "raspberry" in distro.name().lower():
                return True
        except ImportError:
            pass
    except Exception:
        pass

    return False

if __name__ == "__main__":

    logger = logging.getLogger('test logger')
    if is_raspberry_pi():
        target = 'www.viltstigen.se'
        secure = True
    else:
        target = 'localhost:5000'
        secure = False
    
    print(f"Targeting logging server at: {target}")
    http_handler = logging.handlers.HTTPHandler(target, '/logger/log', method='POST', secure=secure)
    logger.addHandler(http_handler)

    logger.warning('Hey log a warning as well')
    logger.error("Hey log a error again")

