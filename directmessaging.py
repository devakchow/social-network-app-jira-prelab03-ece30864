import uuid
from datetime import datetime
from typing import Dict, List, Optional
from math import sqrt


class MessageStub:
    """Represents a dummy data model for a single direct message."""

    def __init__(self, sender_id: str, receiver_id: str, content: str):
        self.message_id: str = str(uuid.uuid4())
        self.sender_id: str = sender_id
        self.receiver_id: str = receiver_id
        self.content: str = content
        self.timestamp: datetime = datetime.utcnow()
        self.is_read: bool = False


class DirectMessagingService:
    """Stubs for managing user connections and direct message routing."""

    def __init__(self):
        # Dummy in-memory storage: { user_id: [MessageStub, ...] }
        self._message_store: Dict[str, List[MessageStub]] = {}
        # Dummy active connections: { user_id: is_online }
        self._active_sessions: Dict[str, bool] = {}

    def connect_user(self, user_id: str) -> bool:
        """Simulates a user logging in or connecting to the DM websocket."""
        self._active_sessions[user_id] = True
        if user_id not in self._message_store:
            self._message_store[user_id] = []
        return True

    def disconnect_user(self, user_id: str) -> None:
        """Simulates a user disconnecting."""
        if user_id in self._active_sessions:
            self._active_sessions[user_id] = False

    def send_direct_message(
        self, sender_id: str, receiver_id: str, content: str
    ) -> Optional[MessageStub]:
        """Stubs the logic to validate, save, and route a new message."""
        if not content.strip():
            return None

        # Build the mock message object
        new_message = MessageStub(sender_id, receiver_id, content)

        # Append to dummy datastore for both users
        self._message_store[sender_id].append(new_message)
        if receiver_id in self._message_store:
            self._message_store[receiver_id].append(new_message)

        # Stub: check if recipient is online to deliver instantly
        if self._active_sessions.get(receiver_id, False):
            # Real implementation would trigger web socket emit here
            pass

        return new_message

    def get_chat_history(
        self, user_a: str, user_b: str, limit: int = 50
    ) -> List[MessageStub]:
        """Fetches the filtered conversations between two specific users."""
        user_messages = self._message_store.get(user_a, [])

        # Filter messages belonging strictly to the conversation between user_a and user_b
        conversation = [
            msg
            for msg in user_messages
            if (msg.sender_id == user_a and msg.receiver_id == user_b)
            or (msg.sender_id == user_b and msg.receiver_id == user_a)
        ]

        # Sort by oldest to newest and apply limit
        conversation.sort(key=lambda x: x.timestamp)
        return conversation[:limit]

    def mark_as_read(self, message_id: str, user_id: str) -> bool:
        """Stubs updating the read receipt status of a message."""
        # Stub logic to locate message and toggle read state
        return True


# ==========================================
# Usage Example
# ==========================================
if __name__ == "__main__":
    dm_system = DirectMessagingService()

    # Connect dummy users
    dm_system.connect_user("alice_123")
    dm_system.connect_user("bob_456")

    # Send a message
    msg = dm_system.send_direct_message(
        sender_id="alice_123",
        receiver_id="bob_456",
        content="Hey Bob! Are we still on for the sync later?",
    )

    print(f"Sent Message ID: {msg.message_id}")
    print(f"Content: '{msg.content}' at {msg.timestamp}")

    # Fetch history
    history = dm_system.get_chat_history("alice_123", "bob_456")
    print(f"Chat history length: {len(history)}")
