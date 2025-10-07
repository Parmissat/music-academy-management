from django.contrib import admin
from .models import Teacher, Student, ClassSession, Attendance, Payment, TeacherSettlement
import jdatetime
from django.db import models
from jalali_date.widgets import AdminJalaliDateWidget

# -------------------- Admin --------------------
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'percentage_share', 'student_count']
    search_fields = ['name', 'phone']
    list_filter = ['percentage_share']

    def student_count(self, obj):
        return obj.student_set.count()
    student_count.short_description = 'تعداد هنرجویان'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'teacher', 'monthly_fee', 'registration_date_shamsi']
    list_filter = ['teacher', 'registration_date']
    search_fields = ['name', 'phone']

    def registration_date_shamsi(self, obj):
        if obj.registration_date:
            return jdatetime.date.fromgregorian(date=obj.registration_date).strftime('%Y/%m/%d')
        return ''
    registration_date_shamsi.short_description = 'تاریخ ثبت‌نام (شمسی)'


@admin.register(ClassSession)
class ClassSessionAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'day_of_week', 'time']
    list_filter = ['teacher', 'day_of_week']
    search_fields = ['student__name', 'teacher__name']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['class_session', 'date_shamsi']
    list_filter = ['date', 'class_session__teacher']
    search_fields = ['class_session__student__name']

    def date_shamsi(self, obj):
        if obj.date:
            return jdatetime.date.fromgregorian(date=obj.date).strftime('%Y/%m/%d')
        return ''
    date_shamsi.short_description = 'تاریخ (شمسی)'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount', 'payment_method_display', 'payment_date_shamsi', 'teacher_share']
    list_filter = ['payment_method', 'payment_date', 'for_year', 'for_month']
    search_fields = ['student__name']

    def payment_method_display(self, obj):
        return dict(Payment.PAYMENT_METHODS).get(obj.payment_method, obj.payment_method)
    payment_method_display.short_description = 'روش پرداخت'

    def payment_date_shamsi(self, obj):
        if obj.payment_date:
            return jdatetime.date.fromgregorian(date=obj.payment_date).strftime('%Y/%m/%d')
        return ''
    payment_date_shamsi.short_description = 'تاریخ پرداخت (شمسی)'


@admin.register(TeacherSettlement)
class TeacherSettlementAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'amount', 'settlement_date_shamsi', 'description_short']
    list_filter = ['settlement_date']
    search_fields = ['teacher__name']

    def settlement_date_shamsi(self, obj):
        if obj.settlement_date:
            return jdatetime.date.fromgregorian(date=obj.settlement_date).strftime('%Y/%m/%d')
        return ''
    settlement_date_shamsi.short_description = 'تاریخ تسویه (شمسی)'

    def description_short(self, obj):
        if obj.description and len(obj.description) > 50:
            return obj.description[:50] + '...'
        return obj.description
    description_short.short_description = 'توضیحات'
