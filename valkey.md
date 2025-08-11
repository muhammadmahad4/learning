---

## **Valkey (Redis alternative): In-memory key-value store for config/event messaging**

### **What is Valkey?**
- **Valkey** is a fast, in-memory database (it is an open-source fork of Redis).
- It's mainly used for caching, storing key-value data, and **realtime messaging/events**.

---

### **What was our use-case?**
- **Store the camera config** (`camera_config` key).
- **Detect and react to changes** (keyspace/keyevent notifications).
- **Send and receive events between services via pub/sub channels.**

---

### **Key Concepts (easy version):**
- **Key-Value Store:**  
  You set and get values (could be strings, JSON, lists, sets) with simple commands.
  - Set: `SET camera_config "some value"`
  - Get: `GET camera_config`
  - Delete: `DEL camera_config`

- **Pub/Sub:**  
  *Publish and Subscribe*:  
  One part of your app can send a message to a "channel"; others can listen and react.
  - Subscribe: `SUBSCRIBE mychannel`
  - Publish: `PUBLISH mychannel "hello"`

- **Keyspace/Keyevent notifications:**  
  Special Valkey/Redis feature: it emits messages when keys are changed, expired, or deleted.
  - Listen for changes: `SUBSCRIBE __keyevent@0__:set`
  - Valkey sends: `"camera_config"` when you update `camera_config`
  - This lets other apps trigger, for example, a restart or a reload.

---

### **Why in-memory?**
- It's super-fast, everything sits in RAM.
- Ideal for temporary state, config, task queues, synchronization, caching.

---

### **How did we use Valkey in code? (Python example)**
```python
from valkey import Valkey

vk = Valkey(host="localhost", port=6379)

vk.set("camera_config", "my new config")
config = vk.get("camera_config")
print(config)  # prints your config

pubsub = vk.pubsub()
pubsub.subscribe("__keyevent@0__:set")
for message in pubsub.listen():
    print(message)
```

---

### **What else can Valkey do?**
- Store lists, sets, hashes (kind of like fast Python dicts/lists)
- Expire keys (auto-remove after a timeout)
- Support task queues, rate limiting, counting, and more

---

## **Summary**
- **Valkey/Redis** is used for extremely fast config/data, messaging, and reactions between processes.
- **Keyspace notifications** allow *any service* to know instantly when a config or data point changes.
- **Pub/Sub** messaging lets you connect everything (microservices, containers) in real time, decoupled and scalable.

---


---

## **Pub/Sub & Keyspace Notifications: Real-time event messaging and change tracking**

---

### **Pub/Sub (Publish & Subscribe):**
- **Pub/Sub is a messaging system built into Valkey/Redis.**  
  It lets pieces of software talk to each other without direct connection.

#### **How it works:**
- **Publisher:** Sends ("publishes") a message to a named channel.
- **Subscriber:** Listens ("subscribes") to one or more channels, and gets any messages published there.

#### **Visual Example:**
```
App1: SUBSCRIBE mychannel
App2: PUBLISH mychannel "message"
# App1 instantly receives "message"
```

**Advantages:**
- Instant, event-driven communication.
- Decouples sender and receiver (don't need direct reference; any number of listeners).

---

### **Keyspace & Keyevent Notifications**  
*(Special Valkey/Redis feature)*

#### **Purpose:**
- Lets apps watch for *changes to data* (keys set, deleted, expired, etc.).
- Useful for triggering events like reload, restart, alert, cache flush.

#### **How it works:**  
When configured, Valkey will "publish" an internal message anytime something happens to a key.

**Example:**  
- Setting `camera_config` with `SET camera_config ...`  
  - Publishes:  
    - Channel: `__keyspace@0__:camera_config`, message: `set` (*all events about this key*)
    - Channel: `__keyevent@0__:set`, message: `camera_config` (*all set events on any key*)

**So in code:**
```python
pubsub.subscribe("__keyevent@0__:set")
for msg in pubsub.listen():
    if msg["data"] == "camera_config":
        print("camera_config was set!")
```
Or:
```python
pubsub.subscribe("__keyspace@0__:camera_config")
for msg in pubsub.listen():
    if msg["data"] == "set":
        print("camera_config changed!")
```

---

**Difference Between Pub/Sub and Keyspace Notifications:**

| Feature        | Pub/Sub                               | Keyspace Notification                 |
|----------------|--------------------------------------|---------------------------------------|
| Who triggers?  | Your app (PUBLISH)                   | Valkey itself (when key changes)      |
| What channels? | Freely chosen, like "alerts"         | System channels, like "__keyevent@0__..." |
| Used for?      | Custom messages                      | Internal change events (SET, DEL, etc)|
| Reliable?      | Fire & forget                        | Fire & forget (no history queued)     |

---

## **Summary**

- **Pub/Sub:** You send/receive custom channels/messaging between apps.
- **Keyspace notifications:** Valkey/Reds system can signal when keys are changed/deleted, used for triggers.
- **We used both to restart containers or react to changes!**

---
