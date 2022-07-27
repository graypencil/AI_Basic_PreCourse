# Teacher's Solve

class Note(object):
    def __init__(self, content = None):
        self.content = content
        
    def write_content(self, content):
        self.content = content
        
    def remove_all(self):
        self.content = ""
        
    def __add__(self, other):
        return self.content + other.content
    
    def __str__(self):
        return "노트에 적힌 내용: {0}".format(
            self.content)
        
class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}
        
    def add_note(self, note, page = 0): # 이 부분이 문제. 항상 이 함수 들어갈 땐 초기화된 값으로 나오는 것 같음.
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note} # 값 지정의 경우, reset 되는 경우가 있어서 update()도 고민해보았음.
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")
                
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")
            
    def get_number_of_pages(self):
        return len(self.notes.keys())