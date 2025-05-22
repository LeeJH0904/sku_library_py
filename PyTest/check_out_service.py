class CheckOutService:
    def create_checkout(self, user_id,book_id):
        return f"{user_id}_{book_id}_checkout"