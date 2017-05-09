class Book(object):
	#Book class constructor
	def __init__(self, chapters, number_pages, title):
		self.__chapters = chapters
		self.__title = title
		self.__number_pages = number_pages
	# method to show the number of pages contained in a particular book
	def getPages(self):
		return self.__number_pages
	# method to shoe number of chapters in a book
	def getChapters(self):
		return self.__chapters
	#method to get books title
	def getTitle(self):
		return self.__title
# Child class inheriting from parent class
class Book_Gerner(Book):
	def __init__(self, title, chapters, number_pages, gerner):
		super().__init__( chapters, title, number_pages)
		self.__gerner = gerner
	#method to retun book description containing number of chapters, number of pages, gerner and book title
	def book_description(self):
		return "The book entitled " + self.getTitle() + " has " + self.getChapters() + " chapters, " + self.getPages() + " number of pages and is of the category " + self.__gerner

class Main_Charecter(Book_Gerner):
	def __init__(self):
		self.character_Name = "Mon Petite"
	def book_description(self):
		return "The books main character of the book is" + self.character_Name
b = Book_Gerner( "12", "Lady in Red", "234", "Thriller")
print(b.book_description())
c = Main_Charecter()
c.book_description()
