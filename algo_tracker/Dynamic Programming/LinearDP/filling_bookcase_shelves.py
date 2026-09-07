from functools import lru_cache
class BookCaseShelves:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        @lru_cache()
        def get_min_height(num_books, remaining_width, h = 0):
            if(num_books == len(books)):
                return h
            
            height = h+ get_min_height(num_books+1, shelfWidth-books[num_books][0],books[num_books][1])
            if books[num_books][0] <= remaining_width:
                height = min(height,get_min_height(num_books+1, remaining_width-books[num_books][0], max(books[num_books][1], h)))
            return height
        return get_min_height(0, shelfWidth)