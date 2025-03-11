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
         {"title": "오셸로", "author": "셰익스피어", "publisher": "문학수첩", "genre": "역사"}]
    
loan_history = {}
genre_count = {}

# 메뉴
display = '''
-------------------------------------------------------------
1. 도서 등록 | 2. 도서 목록 조회 | 3. 도서 검색  
4. 대출 실행 | 5. 대출 도서 목록 | 6. 도서 반납 | 7. 종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

while True:
    menu = input(display).strip()

    # 도서 등록
    if menu == '1':
        title = input("책 제목을 입력하세요: ")
        author = input("저자를 입력하세요: ")
        publisher = input("출판사를 입력하세요: ")
        genre = input("장르를 입력하세요: ")
        
        # 입력받은 정보로 도서 추가
        books.append({"title": title, "author": author, "publisher": publisher, "genre": genre})
        print(f"'{title}' 책이 등록되었습니다.")
        
    # 2. 도서 목록 조회
    elif menu == '2':
        print("\n등록된 책 목록:")
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. {book['title']} - {book['author']} ({book['publisher']})")

    # 3. 도서 검색
    elif menu == '3':
        print('도서 검색')
        keyword = input("검색할 내용을 입력하세요. (제목, 저자, 출판사, 장르) ").strip().lower()
        a = False

        print("\n검색 결과")
        for idx, book in enumerate(books, start=1):
            if (keyword in book['title'].lower() or 
                keyword in book['author'].lower() or 
                keyword in book['publisher'].lower() or 
                keyword in book['genre'].lower()):
                print(f"{idx}. {book['title']} - {book['author']} ({book['publisher']}) - 장르: {book['genre']}")
                a = True
        if not a:
            print("검색 결과가 없습니다.")
        
    # 4. 대출 실행
    elif menu == '4':
        print('프로그램 종료')

    # 5. 대출 도서 목록
    elif menu == '5':
        print('프로그램 종료')

    # 6. 도서 반납
    elif menu == '6':
        print('프로그램 종료')

    elif menu == '7':
        print('프로그램 종료')
        sys.exit()

    # 잘못된 입력 처리
    else:
        print("메뉴 선택을 잘못하셨습니다.")