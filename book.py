import sys
# 도서 목록과 관련된 데이터
books = []
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
         search_term = input("검색할 책 제목, 저자, ISBN 등을 입력하세요: ").lower()
         found_books = [book for book in books if search_term in book['title'].lower() or search_term in book['author'].lower()]
        
         if found_books:
             print("\n검색 결과:")
             for book in found_books:
                 print(f"{book['title']} - {book['author']} ({book['publisher']})")
         else:
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