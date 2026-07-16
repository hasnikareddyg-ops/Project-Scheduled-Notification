import subprocess
import os

project_path = os.path.dirname(os.path.abspath(__file__))

scheduler_path = os.path.join(project_path, "scheduler.py")

subprocess.Popen(["python", scheduler_path])