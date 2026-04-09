import json

DATA_FILE = "friends.json"

def readAll():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def saveAll(friends):
    with open(DATA_FILE, "w") as f:
        json.dump(friends, f, indent=4)

def add(name, phone, github):
    friends = readAll()
    friends.append({"name": name, "phone": phone, "github": github})
    saveAll(friends)
    print(f"{name} added successfully.")

def remove(name):
    friends = readAll()
    updated = [f for f in friends if f["name"] != name]
    saveAll(updated)
    print(f"{name} removed successfully.")

def updatePhone(name, phone):
    friends = readAll()
    for f in friends:
        if f["name"] == name:
            f["phone"] = phone
            print(f"Phone updated for {name}")
            break
    saveAll(friends)

def updateGithub(name, github):
    friends = readAll()
    for f in friends:
        if f["name"] == name:
            f["github"] = github
            print(f"GitHub updated for {name}")
            break
    saveAll(friends)

def printByName(name):
    friends = readAll()
    for f in friends:
        if f["name"] == name:
            print(f)
            return
    print("Friend not found.")

def printAll():
    friends = readAll()
    for f in friends:
        print(f)

if __name__ == "__main__":
    add("Jaimin", "9876543210", "jaiminGit")
    add("Raj", "9988776655", "raj123")
    printAll()
    updatePhone("Jaimin", "9123456789")
    updateGithub("Raj", "rajNewHub")
    printByName("Raj")
    remove("Jaimin")
    printAll()
