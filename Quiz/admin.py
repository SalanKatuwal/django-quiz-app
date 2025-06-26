from django.contrib import admin
from .models import Quiz,CustomUser,score,EmailOtp
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_verified', 'is_staff')
    list_filter = ('is_verified', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display=('question', 'option1', 'option2', 'option3', 'option4')
    list_filter=('category', 'difficulty')
    search_fields=('question',)

admin.site.register(Quiz,QuizAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'difficulty', 'score')
    list_filter = ('category', 'difficulty')
    search_fields = ('user__username',)
admin.site.register(score, ScoreAdmin)

class EmailOtpAdmin(admin.ModelAdmin):
    list_display = ('email', 'otp', 'created_at')
    search_fields = ('email',)
admin.site.register(EmailOtp, EmailOtpAdmin)