# 🌐 **Podman Main Commands Cheat-Sheet**

### ⚡️ **Container Lifecycle**

```bash
podman run IMAGE                         # Run a container from IMAGE (in foreground)
podman run -d --name CONTAINER IMAGE     # Run detached with a name
podman stop CONTAINER                    # Stop a running container
podman start CONTAINER                   # Start a stopped container
podman restart CONTAINER                 # Restart a running container
podman rm CONTAINER                      # Remove (delete) a container
podman ps                                # List running containers
podman ps -a                             # List all containers (including stopped)
```

---

### 🧳 **Building & Images**

```bash
podman build -t NAME .                   # Build image from Dockerfile in current directory
podman images                            # List all local images
podman rmi IMAGE                         # Remove (delete) an image
podman pull IMAGE                        # Download an image from registry (Docker Hub etc)
podman tag IMAGE NEWNAME                 # Tag image with a different name
```

---

### 🔗 **Exec & Shell into Containers**

```bash
podman exec -it CONTAINER bash           # Start a bash shell inside CONTAINER
podman exec -it CONTAINER sh             # If bash isn't present, use sh
podman exec -it CONTAINER COMMAND        # Run any command (e.g., valkey-cli)
```

---

### 📤 **Logs & Output**

```bash
podman logs CONTAINER                    # Show logs/output from container
podman logs -f CONTAINER                 # Show logs and follow ("tail -f" style)
```

---

### 🌐 **Container Networking**

```bash
podman run -p HOSTPORT:CONTAINERPORT ... # Map ports between host and container
podman port CONTAINER                    # Show port mappings for container
```

---

### 📦 **Volumes/files**

```bash
podman run -v /host/path:/container/path IMAGE   # Mount volume from host to container
podman cp CONTAINER:/container/path /host/path   # Copy files/folders from container to host
podman cp /host/path CONTAINER:/container/path   # Copy files into container
```

---

### 📊 **Inspect, Info & Stats**

```bash
podman inspect CONTAINER                   # Detailed info about a container (JSON)
podman stats                               # Real-time container resource usage
podman info                                # Info about Podman setup and host
```

---

### 🔒 **System Prune/Cleanup**

```bash
podman prune                               # Remove unused data (containers, images, volumes)
podman system prune                        # Remove all unused containers, images, networks
```

---

### 👥 **Pod Management**

```bash
podman pod create --name PODNAME           # Create a new pod (multi-container group)
podman pod ps                              # List running pods
podman run --pod PODNAME IMAGE             # Run containers inside a pod
```

---

# 🗂️ **Ready-to-Save: Podman Command Reference**

Copy-paste the above (or let me know if you need it as a text file or markdown)!

---

