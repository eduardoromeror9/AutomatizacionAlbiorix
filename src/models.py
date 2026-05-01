from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ChatItem:
    name: str
    is_group: bool = False
    raw_title: str = ""

@dataclass
class MessageItem:
    chat_name: str
    message_text: str
    sender: str = ""
    message_date: str = ""
    message_time: str = ""
    raw_meta: str = ""

@dataclass
class ParsedRecord:
    execution_date: str
    group_name: str
    chat_name: str
    message_date: str
    message_time: str
    sender: str
    detected_name: str
    detected_rut: str
    category: str
    variant: str
    status: str
    message_text: str
    notes: str = ""

@dataclass
class RunSummary:
    total_chats_seen: int = 0
    total_groups_processed: int = 0
    total_messages_read: int = 0
    total_records: int = 0
    total_ambiguous: int = 0
    errors: list = field(default_factory=list)
    processed_groups: list = field(default_factory=list)
