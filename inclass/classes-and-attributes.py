class LibraryItem:
    def __init__(self, title:str, author_artist:str, item_id:int):
        self.title = title
        self.author_artist = author_artist
        self.item_id = item_id
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} is checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} is returned.")
        else:
            print(f"{self.title} was not checked out.")

class Book(LibraryItem):
    def __init__(self, title:str, author_artist:str, item_id:int, isbn:int):
        super().__init__(title, author_artist, item_id)
        self.isbn = isbn