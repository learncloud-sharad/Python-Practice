print("## First Example")
rows  = 1500
if rows == 0:
    status = 'EMPTY'
elif rows < 1000:
    status = 'SMALL'
else:
    status = 'OK'
print(status)
print("\n ==========================================")
print("\n## Second Example")

for name in ['a.csv','notes.txt','c.csv']:
    if not name.endswith('.csv'):
        continue
    print("Loading...", name)

print("\n ==========================================")
print("\n## Third Example")
attempts = 0
while attempts < 3:
    attempts = attempts + 1
    print(attempts)