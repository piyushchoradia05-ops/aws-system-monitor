from flask import Flask, render_template
import psutil
import time

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    uptime = int(time.time() - start_time)

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory.percent,
        disk=disk.percent,
        uptime=uptime
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)