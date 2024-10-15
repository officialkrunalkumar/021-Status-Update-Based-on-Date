from datetime import datetime
def main(event):
  tsd = int(event.get("inputFields").get("tsd"))
  status = event.get("inputFields").get("status")
  today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
  timestamp = int(today.timestamp() * 1000)
  if tsd == timestamp:
    status = "in_progress"
  return {
    "outputFields": {
      "status": status
    }
  }