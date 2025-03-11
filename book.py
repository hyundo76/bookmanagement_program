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

# 도서 등록
books.append({"title": "파이썬 프로그래밍", "author": "홍길동", "publisher": "파이썬출판사", "genre": "IT"})
books.append({"title": "알고리즘", "author": "김철수", "publisher": "알고리즘출판사", "genre": "IT"})
books.append({"title": "어린 왕자", "author": "생텍쥐페리", "publisher": "문학출판사", "genre": "문학"})

# 도서 목록 조회
print("등록된 책 목록:")
for idx, book in enumerate(books, start=1):
    print(f"{idx}. {book['title']} - {book['author']} ({book['publisher']})")

# 도서 검색
keyword = "파이썬"
print(f"\n'{keyword}'에 대한 검색 결과:")
for book in books:
    if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
        print(f"{book['title']} - {book['author']} ({book['publisher']})")

# 대출 관리
title_to_loan = "파이썬 프로그래밍"
user_to_loan = "박지민"

if any(book['title'] == title_to_loan for book in books):
    if title_to_loan not in loan_history:
        loan_history[title_to_loan] = user_to_loan
        print(f"\n'{title_to_loan}' 책이 {user_to_loan}에게 대출되었습니다.")
    else:
        print(f"\n'{title_to_loan}' 책은 이미 대출 중입니다.")
else:
    print(f"\n'{title_to_loan}' 책은 등록되지 않았습니다.")

# 반납 관리
title_to_return = "파이썬 프로그래밍"
if title_to_return in loan_history:
    user = loan_history.pop(title_to_return)
    print(f"\n'{title_to_return}' 책이 {user}로부터 반납되었습니다.")
else:
    print(f"\n'{title_to_return}' 책은 대출 중이지 않습니다.")

# 통계 기능: 장르별 책 수
print("\n장르별 통계:")
for book in books:
    genre = book['genre']
    if genre not in genre_count:
        genre_count[genre] = 0
    genre_count[genre] += 1

for genre, count in genre_count.items():
    print(f"{genre}: {count}권")
