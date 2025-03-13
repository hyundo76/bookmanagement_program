import sys


def addBook():
    title = input("책 제목을 입력하세요: ")
    author = input("저자를 입력하세요: ")
    publisher = input("출판사를 입력하세요: ")
    genre = input("장르를 입력하세요: ")

    # 입력받은 정보로 도서 추가, append 함수로 books 리스트에 딕셔너리 추가
    books.append(
        {"title": title, "author": author, "publisher": publisher, "genre": genre}
    )
    return title


def getBookList(bookss):
    print("\n등록된 책 목록:")
    for idx, book in enumerate(bookss, start=1):
        print(f"{idx}. {book['title']} - {book['author']} ({book['publisher']})")


def researchbook(keyword):
    a = False
    book01 = []

    print("\n검색 결과")
    for idx, book in enumerate(books, start=1):
        if (
            keyword in book["title"].lower()
            or keyword in book["author"].lower()
            or keyword in book["publisher"].lower()
            or keyword in book["genre"].lower()
        ):
            book01.append(book)
            a = True

    return book01, a


def checkLoanAvailability(title_to_loan):
    # 대출할 책이 있는지 확인
    book_found = None
    for book in books:
        if book["title"] == title_to_loan:
            book_found = book
            break
    return book_found


def loanBook(book_found):
    if book_found:
        # 책이 존재하고 대출되지 않았다면 대출자 정보 입력, loan_history 딕셔너리에 대출 정보 저장
        if title_to_loan not in loan_history:
            borrower = input(
                f"'{title_to_loan}' 책을 대출할 사람의 이름을 입력하세요: "
            )
            loan_history[title_to_loan] = borrower
            print(f"'{title_to_loan}' 책이 {borrower}에게 대출되었습니다.")
        else:
            print(f"'{title_to_loan}' 책은 이미 대출 중입니다.")
    else:
        print(f"'{title_to_loan}' 책은 등록되지 않았습니다.")

def process_book_return(loan_borrower,loan_title):

    for title, borrower in loan_history.items():
        if loan_borrower == borrower and loan_title == title:
            del loan_history[loan_title]
            print("반납되셨습니다.")
            break
        else:
            print("맞는 책이 존재하지 않습니다.")

def display_loaned_books(loan_history):
    print("대출 도서 목록")
    if loan_history:
        for title, borrower in loan_history.items():
            print(f"{title} - {borrower}")
    else:
        print("대출목록없음")


# 도서 목록과 관련된 데이터
books = [
    {
        "title": "해리포터",
        "author": "조앤 롤링",
        "publisher": "문학수첩",
        "genre": "판타지",
    },
    {
        "title": "반지의 제왕",
        "author": "톨킨",
        "publisher": "문학수첩",
        "genre": "판타지",
    },
    {
        "title": "죽은 시인의 사회",
        "author": "피터 와이어",
        "publisher": "문학수첩",
        "genre": "드라마",
    },
    {
        "title": "노인과 바다",
        "author": "헤밍웨이",
        "publisher": "문학수첩",
        "genre": "드라마",
    },
    {"title": "1984", "author": "조지 오웰", "publisher": "문학수첩", "genre": "SF"},
    {
        "title": "페스트",
        "author": "알베르 카뮈",
        "publisher": "문학수첩",
        "genre": "소설",
    },
    {
        "title": "동물농장",
        "author": "조지 오웰",
        "publisher": "문학수첩",
        "genre": "소설",
    },
    {
        "title": "죄와 벌",
        "author": "톨스토이",
        "publisher": "문학수첩",
        "genre": "소설",
    },
    {
        "title": "어린왕자",
        "author": "생텍쥐페리",
        "publisher": "문학수첩",
        "genre": "동화",
    },
    {
        "title": "백설공주",
        "author": "그림형제",
        "publisher": "문학수첩",
        "genre": "동화",
    },
    {
        "title": "신데렐라",
        "author": "그림형제",
        "publisher": "문학수첩",
        "genre": "동화",
    },
    {"title": "흥부전", "author": "흥부", "publisher": "문학수첩", "genre": "동화"},
    {"title": "홍길동전", "author": "홍길동", "publisher": "문학수첩", "genre": "동화"},
    {"title": "햄릿", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"},
    {
        "title": "맥베스",
        "author": "셰익스피어",
        "publisher": "문학수첩",
        "genre": "역사",
    },
    {
        "title": "오셸로",
        "author": "셰익스피어",
        "publisher": "문학수첩",
        "genre": "역사",
    },
    {
        "title": "리어왕",
        "author": "셰익스피어",
        "publisher": "문학수첩",
        "genre": "역사",
    },
    {"title": "햄릿", "author": "셰익스피어", "publisher": "북플러스", "genre": "역사"},
    {
        "title": "맥베스",
        "author": "셰익스피어",
        "publisher": "다빈소년",
        "genre": "역사",
    },
    {
        "title": "오셸로",
        "author": "셰익스피어",
        "publisher": "부경서점",
        "genre": "역사",
    },
    {
        "title": "리어왕",
        "author": "셰익스피어",
        "publisher": "북플러스",
        "genre": "역사",
    },
    {
        "title": "데미안",
        "author": "헤르만 헤세",
        "publisher": "문학좋아",
        "genre": "소설",
    },
    {
        "title": "싯다르타",
        "author": "헤르만 헤세",
        "publisher": "문학싫어",
        "genre": "소설",
    },
    {
        "title": "구토",
        "author": "장뽈 샤르트",
        "publisher": "좋은사람들",
        "genre": "소설",
    },
    {
        "title": "이방인",
        "author": "알베르 카뮈",
        "publisher": "문학수첩",
        "genre": "소설",
    },
]

loan_history = {
    "맥베스": "박현도",
    "오셸로": "정지우",
    "오셸로": "박현도",
    "리어왕": "백경이",
    "흥부전": "백경이",
    "햄릿": "이수연",
    "페스트": "이수연",
}

# 메뉴
display = """
-------------------------------------------------------------
1. 도서 등록 | 2. 도서 목록 조회 | 3. 도서 검색  
4. 대출 실행 | 5. 대출 도서 목록 | 6. 도서 반납 | 7. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> """

while True:
    menu = input(display).strip()

    # 도서 등록
    if menu == "1":
        title = addBook()

        print(f"'{title}' 책이 등록되었습니다.")

    # 2. 도서 목록 조회, enumerate 함수로 인덱스 번호를 붙여서 출력
    elif menu == "2":
        getBookList(books)

    # 3. 도서 검색, 검색어를 입력받아 검색 결과 출력, or 조건문으로 검색어가 포함된 모든 책 출력
    elif menu == "3":
        print("도서 검색")
        keyword = (
            input("검색할 내용을 입력하세요. (제목, 저자, 출판사, 장르) ")
            .strip()
            .lower()
        )

        book01, a = researchbook(keyword)
        if not a:
            print("검색결과가 없습니다.")

        getBookList(book01)

    # 4. 대출 실행, 대출할 책 제목을 입력받아 대출자 정보 입력, 플래그 변수[none/ 값 있음]로 책 보유 유무 확인,
    elif menu == "4":
        title_to_loan = input("대출할 책 제목을 입력하세요: ")

        book_found = checkLoanAvailability(title_to_loan)

        loanBook(book_found)

    # 5. 대출 도서 목록, loan_history 딕셔너리 출력
    elif menu == "5":
        display_loaned_books(loan_history)


    # 6. 도서 반납, 대출자 이름과 반납할 책 제목 입력, del 함수로 loan_history 딕셔너리에서 삭제
    elif menu == "6":
        print("도서 반납")
        display_loaned_books(loan_history)
        
        loan_borrower = input("대출자 성함을 입력하세요. ")
        loan_title = input("반납할 도서를 입력하세요. ")
        
        process_book_return(loan_borrower,loan_title)

    elif menu == "7":
        print("프로그램 종료")
        sys.exit()

    # 잘못된 입력 처리
    else:
        print("메뉴 선택을 잘못하셨습니다.")
