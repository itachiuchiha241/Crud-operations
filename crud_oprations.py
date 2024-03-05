class CRUD:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        self.data[key] = value

    def read(self, key):
        return self.data.get(key)

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            print("Key does not exist.")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
        else:
            print("Key does not exist.")

    def display_all(self):
        for key, value in self.data.items():
            print(f"{key}: {value}")
