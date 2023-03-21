from _collections import deque
bank = deque(["Anis","Karim","Bijoy"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank:
    print("No person left")