from app import LibraryApp

app = LibraryApp()
app.start()  # 서비스 초기화

# 로그인 흐름

userid = input("아이디를 입력하세요. (ex: user1): ")
userPW = input("비밀번호를 입력하세요. (ex: password123): ")
if app.login(userid, userPW):
    # 도서 검색
    bookName = input("검색어를 입력하세요. (ex: 파이썬): ")
    books = app.search_books(bookName)

    bookid = input("\n대출할 책의 id를 입력하세요. (ex: book1):")

    # 대출 요청
    if bookid in books:
        app.request_checkout("user1", "book1")