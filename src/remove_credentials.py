import os

creds = [l.split("Target: ")[1].strip() for l in os.popen("cmdkey /list").readlines() if l.strip().startswith("Target")]
for cred in creds:
    os.system("cmdkey /delete:%s" % cred)