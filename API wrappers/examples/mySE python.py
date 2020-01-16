import mySe
from time import sleep

local_url, mail = "http://127.0.0.1:5000/", "mail@mail.mail"

# Generate a token:
mySe.gen_token(local_url, mail)
# token = mySe.gen_token(local_url, mail)

# Fetch our token:
token = mySe.get_token(local_url, mail)

# Create our client object.
client = mySE.Client(local_url, token)

print(f"Client ID: {client.id}")
print(f"This secret token: {token}")

# Create a log:
mySe.add_log(False)
sleep(1.2)
mySe.add_log(True)

# Display our logs:
print(f"Log information: ({len(client.logs)})")
count = 0
for log in client.logs:
    print(f"Log {count} | ID: {log.id};")
    print(f"Log {count} | Time: {log.time.strftime('%d/%m/%Y | %H:%M:%S')}")
    print(f"Log {count} | The light was {'on' if log.light else 'off'}!")
