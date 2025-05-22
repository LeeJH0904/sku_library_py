from check_out_service import CheckOutService
from login_service import LoginService
from book_search_service import BookSearchService

class LibraryApp:
    def start(self):
        self.check_out_service = CheckOutService()
        self.book_search_service = BookSearchService()
        self.login_service = LoginService()
        # 앱 시작 시 전체 도서 목록 출력
        self.book_search_service.print_all_books()

    def login(self, user_id, password):
        if self.login_service.accountCheck(user_id, password):
            print("로그인 성공")
            return True
        else:
            print("로그인 실패")
            return False
        
    def search_books(self, keyword):
        results = self.book_search_service.search_books_name(keyword)
        for book_id, info in results.items():
            print(f"[{book_id}] {info['title']} - {'대출 가능' if info['available'] else '대출 불가'}")
        return results
    
    def request_checkout(self, user_id, book_id):
        if not self.book_search_service.is_available(book_id):
            print("대출 불가: 책이 이미 대출 중입니다.")
            return None
        
        checkout_id = self.check_out_service.create_checkout(user_id, book_id)
        if checkout_id:
            # 대출 성공 시 도서 상태 업데이트
            self.book_search_service.update_book_status(book_id, False)
            print(f"대출 성공! 대출 ID: {checkout_id}")
            # 업데이트된 도서 목록 출력
            print("\n=== 대출 후 도서 목록 ===")
            self.book_search_service.print_all_books()
            return checkout_id
        return None