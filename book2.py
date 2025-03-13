import sys

# 도서 목록과 관련된 데이터
books = [{"title": "해리포터", "author": "조앤 롤링", "publisher": "문학수첩", "genre": "판타지"},
         {"title": "반지의 제왕", "author": "톨킨", "publisher": "문학수첩", "genre": "판타지"}, 
         {"title": "죽은 시인의 사회", "author": "피터 와이어", "publisher": "문학수첩", "genre": "드라마"},
         {"title": "노인과 바다", "author": "헤밍웨이", "publisher": "문학수첩", "genre": "드라마"},
         {"title": "1984", "author": "조지 오웰", "publisher": "문학수첩", "genre": "SF"},
         {"title": "페스트", "author": "알베르 카뮈", "publisher": "문학수첩", "genre": "소설"},
         {"title": "동물농장", "author": "조지 오웰", "publisher": "문학수첩", "genre": "소설"},
         {"title": "죄와 벌", "author": "톨스토이", "publisher": "문학수첩", "genre": "소설"},
         {"title": "어린왕자", "author": "생텍쥐페리", "publisher": "문학수첩", "genre": "동화"},
         {"title": "백설공주", "author": "그림형제", "publisher": "문학수첩", "genre": "동화"},
         {"title": "신데렐라", "author": "그림형제", "publisher": "문학수첩", "genre": "동화"},
         {"title": "흥부전", "author": "흥부", "publisher": "문학수첩", "genre": "동화"},
         {"title": "홍길동전", "author": "홍길동", "publisher": "문학수첩", "genre": "동화"},
         {"title": "햄릿", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"},
         {"title": "맥베스", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"},
         {"title": "오셸로", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"},
         {"title": "리어왕", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"},
         {"title": "햄릿", "author": "셰익스피어", "publisher": "북플러스", "genre": "역사"},
         {"title": "맥베스", "author": "셰익스피어", "publisher": "다빈소년", "genre": "역사"},
         {"title": "오셸로", "author": "셰익스피어", "publisher": "부경서점", "genre": "역사"},
         {"title": "리어왕", "author": "셰익스피어", "publisher": "북플러스", "genre": "역사"},
         {"title": "데미안", "author": "헤르만 헤세", "publisher": "문학좋아", "genre": "소설"},
         {"title": "싯다르타", "author": "헤르만 헤세", "publisher": "문학싫어", "genre": "소설"},
         {"title": "구토", "author": "장뽈 샤르트", "publisher": "좋은사람들", "genre": "소설"},
         {"title": "이방인", "author": "알베르 카뮈", "publisher": "문학수첩", "genre": "소설"}]

# loan_history는 이제 책 제목 대신 인덱스를 키로 사용
loan_history = {14: "박현도", 15: "정지우", 16: "백경이", 11: "이수연"}  # 예시 데이터 (인덱스 기반)

# 메뉴
display = '''
-------------------------------------------------------------
1. 도서 등록 | 2. 도서 목록 조회 | 3. 도서 검색  
4. 대출 실행 | 5. 대출 도서 목록 | 6. 도서 반납 | 7. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

while True:
    menu = input(display).strip()

    # 1. 도서 등록
    if menu == '1':
        title = input("책 제목을 입력하세요: ")
        author = input("저자를 입력하세요: ")
        publisher = input("출판사를 입력하세요: ")
        genre = input("장르를 입력하세요: ")
        books.append({"title": title, "author": author, "publisher": publisher, "genre": genre})
        print(f"'{title}' 책이 등록되었습니다.")

    # 2. 도서 목록 조회
    elif menu == '2':
        print("\n등록된 책 목록:")
        for idx, book in enumerate(books, start=0):  # 인덱스를 0부터 시작
            status = "대출 중" if idx in loan_history else "대출 가능"
            print(f"[{idx}] {book['title']} - {book['author']} ({book['publisher']}) - {status}")

    # 3. 도서 검색
    elif menu == '3':
        print('도서 검색')
        keyword = input("검색할 내용을 입력하세요. (제목, 저자, 출판사, 장르) ").strip().lower()
        found = False
        print("\n검색 결과:")
        for idx, book in enumerate(books, start=0):
            if (keyword in book['title'].lower() or 
                keyword in book['author'].lower() or 
                keyword in book['publisher'].lower() or 
                keyword in book['genre'].lower()):
                status = "대출 중" if idx in loan_history else "대출 가능"
                print(f"[{idx}] {book['title']} - {book['author']} ({book['publisher']}) - 장르: {book['genre']} - {status}")
                found = True
        if not found:
            print("검색 결과가 없습니다.")

    # 4. 대출 실행 (인덱스 기반)
    elif menu == '4':
        title_to_loan = input("대출할 책 제목을 입력하세요: ").strip()
        print("\n대출 가능한 책 목록:")
        found_books = []
        for idx, book in enumerate(books, start=0):
            if title_to_loan.lower() in book['title'].lower():
                status = "대출 중" if idx in loan_history else "대출 가능"
                print(f"[{idx}] {book['title']} - {book['author']} ({book['publisher']}) - {status}")
                found_books.append(idx)

        if found_books:
            try:
                book_idx = int(input("대출할 책의 인덱스를 입력하세요: "))
                if book_idx in found_books:
                    if book_idx not in loan_history:
                        borrower = input(f"'{books[book_idx]['title']}' 책을 대출할 사람의 이름을 입력하세요: ")
                        loan_history[book_idx] = borrower
                        print(f"'{books[book_idx]['title']}' 책이 {borrower}에게 대출되었습니다.")
                    else:
                        print(f"'{books[book_idx]['title']}' 책은 이미 대출 중입니다.")
                else:
                    print("잘못된 인덱스입니다.")
            except ValueError:
                print("인덱스는 숫자여야 합니다.")
        else:
            print(f"'{title_to_loan}' 책은 등록되지 않았습니다.")

    # 5. 대출 도서 목록
    elif menu == '5':
        print('\n대출 도서 목록:')
        if loan_history:
            for idx, borrower in loan_history.items():
                book = books[idx]
                print(f"[{idx}] {book['title']} - {book['author']} ({book['publisher']}) - 대출자: {borrower}")
        else:
            print("대출된 책이 없습니다.")

    # 6. 도서 반납 (인덱스 기반)
    elif menu == '6':
        print('\n도서 반납')
        if loan_history:
            print("대출 도서 목록:")
            for idx, borrower in loan_history.items():
                book = books[idx]
                print(f"[{idx}] {book['title']} - {book['author']} ({book['publisher']}) - 대출자: {borrower}")
            try:
                return_idx = int(input("반납할 책의 인덱스를 입력하세요: "))
                if return_idx in loan_history:
                    borrower = input("대출자 성함을 입력하세요: ")
                    if loan_history[return_idx] == borrower:
                        del loan_history[return_idx]
                        print(f"'{books[return_idx]['title']}' 책이 반납되었습니다.")
                    else:
                        print("대출자 이름이 일치하지 않습니다.")
                else:
                    print("해당 인덱스의 책은 대출 중이 아닙니다.")
            except ValueError:
                print("인덱스는 숫자여야 합니다.")
        else:
            print("대출된 책이 없습니다.")

    # 7. 종료
    elif menu == '7':
        print('프로그램 종료')
        sys.exit()

    # 잘못된 입력 처리
    else:
        print("메뉴 선택을 잘못하셨습니다.")