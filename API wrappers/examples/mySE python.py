import mySE
from time import sleep

local_url, mail = "http://127.0.0.1:5000/", "mail@mail.mail"

# Generate a token:
try:
    mySE.gen_token(local_url, mail)
except mySE.error.UnauthorizedError:
    pass
# token = mySe.gen_token(local_url, mail)

# Fetch our token:
token = mySE.get_token(local_url, mail)

# Create our client object.
client = mySE.Client(local_url, token)

print(f"Client ID: {client.id}")
print(f"This secret token: {token}")

# Create 2 logs:
print("\r", "Creating 2 logs...", end=' ')
client.add_log(False)
sleep(1.2)
client.add_log(True)
print("\b\b\b\b: Done.")

# Display our logs:
print(f"Log information: ({len(client.logs)})")
count = 0
for log in client.logs:
    count += 1
    print(f"Log {count} | ID: {log.id};")
    print(f"Log {count} | Time: {log.time.strftime('%d/%m/%Y | %H:%M:%S')}")
    print(f"Log {count} | The light was {'on' if log.light else 'off'}!")
