import random
from datetime import datetime, timedelta

from app.models.event import SecurityEvent


def generate_attack_sequence():

    start_time = datetime.now().replace(microsecond=0)

    source_ip = f"192.168.1.{random.randint(2, 254)}"

    user = random.choice([
        "admin",
        "root",
        "john",
        "alice"
    ])

    delay_1 = random.randint(5, 60)
    delay_2 = random.randint(5, 60)

    port_scan = SecurityEvent(
        event_id="A001",
        event_type="PORT_SCAN",
        timestamp=start_time,
        source_ip=source_ip,
        source_app="nmap",
        target="SSH",
        status="DETECTED"
    )

    failed_login = SecurityEvent(
        event_id="A002",
        event_type="LOGIN_ATTEMPT",
        timestamp=start_time + timedelta(seconds=delay_1),
        source_ip=source_ip,
        source_app="ssh",
        target="SSH",
        status="FAILED",
        user=user
    )

    successful_login = SecurityEvent(
        event_id="A003",
        event_type="LOGIN_ATTEMPT",
        timestamp=start_time + timedelta(
            seconds=delay_1 + delay_2
        ),
        source_ip=source_ip,
        source_app="ssh",
        target="SSH",
        status="SUCCESS",
        user=user
    )

    return [
        port_scan,
        failed_login,
        successful_login
    ]

def generate_normal_sequence(source_ip=None):

    start_time = datetime.now().replace(microsecond=0)

    if source_ip is None:
        source_ip = f"192.168.1.{random.randint(2, 254)}"

    user = random.choice([
        "admin",
        "john",
        "alice",
        "bob"
    ])

    login_delay = random.randint(5, 30)
    file_delay = random.randint(5, 30)

    login = SecurityEvent(
        event_id="N001",
        event_type="LOGIN_ATTEMPT",
        timestamp=start_time,
        source_ip=source_ip,
        source_app="ssh",
        target="SSH",
        status="SUCCESS",
        user=user
    )

    file_access = SecurityEvent(
        event_id="N002",
        event_type="FILE_ACCESS",
        timestamp=start_time + timedelta(seconds=login_delay),
        source_ip=source_ip,
        source_app="file_system",
        target="USER_HOME",
        status="SUCCESS",
        user=user
    )

    http_request = SecurityEvent(
        event_id="N003",
        event_type="HTTP_REQUEST",
        timestamp=start_time + timedelta(
            seconds=login_delay + file_delay
        ),
        source_ip=source_ip,
        source_app="browser",
        target="WEB_SERVER",
        status="SUCCESS",
        user=user
    )

    return [
        login,
        file_access,
        http_request
    ]