from django.contrib import admin
from .models import Borrow

class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'is_returned', 'borrow_date', 'return_date', 'due_date', 'user_reg_no', 'user_name')

admin.site.register(Borrow, BorrowAdmin)


