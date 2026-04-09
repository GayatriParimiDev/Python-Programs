
import json

class FriendAPI:
    def __init__(self, path: str):
        self.path = path
        if not self._exists():
            self.writeAll([])

    def _exists(self) -> bool:
        try:
            with open(self.path, "r", encoding="utf-8"):
                return True
        except FileNotFoundError:
            return False

    def readAll(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def writeAll(self, items):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2)

    def add(self, name, phone, github):
        items = self.readAll()
        items.append({"name": name, "phone": phone, "github": github})
        self.writeAll(items)

    def remove(self, name, phone, github):
        items = self.readAll()
        items = [it for it in items if not (it["name"] == name and it["phone"] == phone and it["github"] == github)]
        self.writeAll(items)

    def updatePhone(self, name, phone):
        items = self.readAll()
        for it in items:
            if it["name"] == name:
                it["phone"] = phone
        self.writeAll(items)

    def updateGithub(self, name, github):
        items = self.readAll()
        for it in items:
            if it["name"] == name:
                it["github"] = github
        self.writeAll(items)

    def printByName(self, name):
        items = self.readAll()
        found = [it for it in items if it["name"] == name]
        if not found:
            print("No friend found with that name.")
        else:
            for it in found:
                print(it)

    def printAll(self):
        items = self.readAll()
        if not items:
            print("No friends in the list.")
        for it in items:
            print(it)

def main():
    api = FriendAPI("friends.json")
    # Start clean
    api.writeAll([])
    api.add("Amrita", "9876543210", "ami-gh")
    api.add("Raj", "9123456780", "raj-dev")
    print("All friends:")
    api.printAll()
    print("Update Raj phone:")
    api.updatePhone("Raj", "9000000000")
    api.printByName("Raj")
    print("Update Amrita github:")
    api.updateGithub("Amrita", "ami-new")
    api.printByName("Amrita")
    print("Remove Amrita:")
    api.remove("Amrita", "9876543210", "ami-new")
    print("Final list:")
    api.printAll()

if __name__ == "__main__":
    main()
