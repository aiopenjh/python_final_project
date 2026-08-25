from models.base_book import Book
from models.specialized_books import EBook, PaperBook
from utils.helpers import validate_input

books_dict = {}
isbn_set = set()
history_list = []


def register_book():
    print("\n--- [도서 등록] ---")
    
    while True:
        print("1. 일반 도서 | 2. 전자도서 | 3. 단행본")
        book_type = input("등록할 도서 종류를 선택하세요 (1/2/3): ").strip()
        if book_type in ["1", "2", "3"]:
            break  # 정상 입력 시 반복 탈출
        print("오류: 1, 2, 3번 중에서만 선택해주세요.\n")

    try:
        isbn = validate_input(input("ISBN 번호 입력: "), "ISBN")
        
        if isbn in isbn_set:
            print("오류: 이미 존재하는 ISBN 번호입니다.")
            return

        title = validate_input(input("도서 제목 입력: "), "제목")
        author = validate_input(input("저자 입력: "), "저자")

        if book_type == "1":
            book = Book(title, author, isbn)
        elif book_type == "2":
            file_size = validate_input(input("파일 크기(예: 10MB): "), "파일 크기")
            book = EBook(title, author, isbn, file_size)
        elif book_type == "3":
            file_size = validate_input(input("파일 크기(예: 10MB): "), "파일 크기")
            book = PaperBook(title, author, isbn, file_size)

        books_dict[isbn] = book
        isbn_set.add(isbn)
        print(f"도서 '{title}' 등록 완료!")

    except ValueError as e:
        print(f" 입력 오류: {e}")

def view_all_books():
    """2. 전체 도서 조회 기능"""
    print("\n--- [전체 도서 목록] ---")
    # 딕셔너리가 비어있는지 확인
    if len(books_dict) == 0:
        print("등록된 도서가 없습니다.")
        return

    # 딕셔너리에 있는 모든 책을 꺼내서 출력
    for book in books_dict.values():
        print(book.get_info())


def search_book():
    """3. 도서 검색 기능"""
    print("\n--- [도서 검색] ---")
    keyword = input("검색할 도서 제목 또는 저자를 입력하세요: ").strip()
    
    if keyword == "":
        print("오류: 검색어를 입력해주세요.")
        return

    found = False
    
    for book in books_dict.values():
        # 제목이나 저자에 검색 단어가 들어있는지 확인
        if (keyword in book.title) or (keyword in book.author):
            print(book.get_info())
            found = True

    if not found:
        print("검색 결과가 없습니다.")


def handle_borrow_return():
    """4. 대여/반납 처리 기능"""
    print("\n--- [대여 / 반납] ---")
    print("1. 대여 | 2. 반납")
    action = input("선택하세요 (1/2): ").strip()

    isbn = input("처리할 도서의 ISBN을 입력하세요: ").strip()

    # 존재하는 ISBN인지 확인
    if isbn not in books_dict:
        print("오류: 등록되지 않은 ISBN입니다.")
        return

    book = books_dict[isbn]

    if action == "1":  # 대여
        if book.borrow():
            # 대여 이력을 튜플 형태로 리스트에 저장
            history_list.append((book.isbn, book.title, "대여"))
            print(f"'{book.title}' 도서가 대여되었습니다.")
        else:
            print("실패: 이미 대여 중인 도서입니다.")

    elif action == "2":  # 반납
        if book.return_book():
            # 반납 이력을 튜플 형태로 리스트에 저장
            history_list.append((book.isbn, book.title, "반납"))
            print(f"'{book.title}' 도서가 반납되었습니다.")
        else:
            print("실패: 대여되지 않은 도서입니다 (반납 불가).")
    else:
        print("오류: 1번 또는 2번을 선택해주세요.")



def main():
    """대화형 콘솔 메뉴(CLI) 반복문"""
    while True:
        print("\n==================================")
        print("     📚 도서 관리 프로그램")
        print("==================================")
        print("1. 도서 등록")
        print("2. 전체 도서 조회")
        print("3. 도서 검색")
        print("4. 대여/반납 처리")
        print("5. 종료")
        print("==================================")
        
        user_choice = input("원하는 메뉴 번호를 입력하세요: ").strip()

        # 잘못된 문자 입력 시 발생할 수 있는 오류 방어
        try:
            menu_num = int(user_choice)
        except ValueError:
            print("오류: 숫자로만 메뉴 번호를 입력해주세요.")
            continue

        if menu_num == 1:
            register_book()
        elif menu_num == 2:
            view_all_books()
        elif menu_num == 3:
            search_book()
        elif menu_num == 4:
            handle_borrow_return()
        elif menu_num == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("오류: 1번부터 5번 사이의 번호를 입력해주세요.")


# 프로그램 실행 진입점
if __name__ == "__main__":
    main()