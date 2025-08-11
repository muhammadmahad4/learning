## 🔹 **Connection**
```bash
valkey-cli                              # Start CLI, connect to local Valkey
valkey-cli -h HOST -p PORT              # Connect to remote Valkey
```

---

## 🔹 **Basic Key-Value Operations**

```bash
SET key value                           # Set value for a key (create/overwrite)
GET key                                 # Get value for a key
DEL key                                 # Delete a key
EXISTS key                              # 1 if key exists, 0 if not
KEYS *                                  # List all keys (use only for debug/small DB)
TTL key                                 # Time-to-live (seconds) left on key
EXPIRE key seconds                      # Set timeout on a key
PERSIST key                             # Remove timeout from a key
```

---

## 🔹 **Strings, Counters**

```bash
INCR key                                # Increment integer value by 1
DECR key                                # Decrement integer value by 1
APPEND key value                        # Append string to value at key
GETSET key value                        # Set new value and return old value
```

---

## 🔹 **Lists**

```bash
LPUSH list value                        # Push value to start of list
RPUSH list value                        # Push value to end of list
LPOP list                               # Remove and return first element
RPOP list                               # Remove and return last element
LRANGE list start stop                  # Get elements in range [start, stop] (LRANGE mylist 0 -1 = all)
LLEN list                               # List length
```

---

## 🔹 **Hashes (like Python dicts)**

```bash
HSET hash field value                   # Set field in hash
HGET hash field                         # Get field value
HGETALL hash                            # Get all fields and values
HDEL hash field                         # Delete a field
```

---

## 🔹 **Sets**

```bash
SADD set member                         # Add member(s) to set
SMEMBERS set                            # Get all members
SREM set member                         # Remove member
SISMEMBER set member                    # 1 if member exists, 0 if not
```

---

## 🔹 **Keyspace Notifications & Pub/Sub**

```bash
CONFIG SET notify-keyspace-events KEA    # Enable keyspace/keyevent notifications
SUBSCRIBE __keyevent@0__:set             # Listen for set events on all keys
SUBSCRIBE __keyspace@0__:mykey           # Listen for changes to mykey
PUBLISH channel message                   # Publish a message on a channel
SUBSCRIBE channel                        # Subscribe/watch a channel
```

---

## 🔹 **Server info & config**

```bash
CONFIG GET notify-keyspace-events        # Show notification settings
INFO                                    # Show server info/stats
FLUSHALL                                # Delete all keys in all databases (CAUTION)
```

---

## 🟢 **Ready-to-save for your file!**

This cheat-sheet covers >95% of daily admin/dev Valkey work.

---

