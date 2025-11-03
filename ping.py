import platform, subprocess
  def ping(host="8.8.8.8", count=4):
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    try:
      print(subprocess.check_output(["ping", flag, str(count), host], text=True))
    except Exception as e:
      print("Ping failed:", e)

if __name__ == "__main__":
  ping()
