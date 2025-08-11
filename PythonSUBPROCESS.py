---

## **Python subprocess module: Calling system/terminal commands from Python**

---

### **What is it?**
- The `subprocess` module lets Python code **run shell/terminal commands**, like you’d type at the command line.

---

### **Why use it?**
- Automate CLI tasks from Python: restart containers, copy files, trigger scripts, etc.
- Example in your project: restart the DeepStream container via Podman.

---

### **Typical usage**

#### **Basic example**
```python
import subprocess

subprocess.run(["ls", "-l"])
```
- Runs `ls -l` in the shell, prints output to console.

#### **Get output to a variable**
```python
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
```
- Runs and captures stdout result.

#### **Run podman restart (like you did!)**
```python
subprocess.run(["podman", "restart", "deepstream"], check=True)
```
- Restarts the container named "deepstream".
- `check=True` makes Python crash if command fails (for error detection).

---

### **Other use-cases**
- Automate backups, data exports, file management.
- Chain together CLI programs for data processing.

---

### **Summary**
- `subprocess.run([...])` lets Python code execute terminal commands.
- Everything shown/logged as if you ran the command by hand.

---

