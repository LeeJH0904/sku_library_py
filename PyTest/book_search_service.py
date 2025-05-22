class BookSearchService:
    def __init__(self):
        self.books = {
            "book1": {"title": "파이썬", "available": True},
            "book2": {"title": "자료구조", "available": False},
            "book3": {"title": "JAVA", "available": True}
        }
    
    def print_all_books(self):
        print("\n=== 전체 도서 목록 ===")
        for book_id, info in self.books.items():
            print(f"[{book_id}] {info['title']} - {'대출 가능' if info['available'] else '대출 불가'}")
        print("===================\n")
    
    def update_book_status(self, book_id, available):
        if book_id in self.books:
            self.books[book_id]['available'] = available
            return True
        return False
    
    def search_books_name(self, keyword):
        result = {}
        for k, v in self.books.items():
            if keyword in v["title"]:
                result[k] = v
        return result
    
    def is_available(self, book_id):
        for key, book in self.books.items():
            if key == book_id:
                if "available" in book:
                    return book["available"]
                else:
                    return False
        return False