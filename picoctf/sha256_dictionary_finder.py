# target hash => e7ae6cfee91a324590df7b048dcc9802b7389c1b0d996d474d61c4cbb1253455

import hashlib

target_hash = "e7ae6cfee91a324590df7b048dcc9802b7389c1b0d996d474d61c4cbb1253455"
with open("/mnt/3cdf242f-56fd-4b8f-95e9-2062d72f0f1e/Security/wordlist/rockyou.txt") as file:
    for line in file:
        stripped = line
        hash = hashlib.sha256(stripped.encode()).hexdigest()
        # print(f"{hash} == {target_hash}")
        if hash == target_hash:
            print(f"Your password is '{stripped}'")
            break