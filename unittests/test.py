import re

pattern = re.compile(r"^(?:[a-z0-9](?:[a-z0-9-_]{0,61}[a-z0-9])?\.)"
                     r"+[a-z0-9][a-z0-9-_]{0,61}[a-z]$")
# domain = "192.168.1.2"
domain = "pos.oneretail.cn"
result = pattern.match(domain.encode("idna").decode("ascii"))

print(result)
