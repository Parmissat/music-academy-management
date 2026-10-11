from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class PersianMonthField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['choices'] = [
            ('01', 'فروردین'),
            ('02', 'اردیبهشت'),
            ('03', 'خرداد'),
            ('04', 'تیر'),
            ('05', 'مرداد'),
            ('06', 'شهریور'),
            ('07', 'مهر'),
            ('08', 'آبان'),
            ('09', 'آذر'),
            ('10', 'دی'),
            ('11', 'بهمن'),
            ('12', 'اسفند')
        ]
        kwargs['verbose_name'] = 'ماه آموزشی'
        super().__init__(*args, **kwargs)


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام استاد')
    phone = models.CharField(max_length=15, verbose_name='شماره تماس')
    percentage_share = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='درصد سهم استاد',
        help_text='درصدی که استاد از هر پرداخت دریافت می‌کند (بین 0 تا 100)'
    )

    class Meta:
        verbose_name = 'استاد'
        verbose_name_plural = 'اساتید'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام هنرجو')
    phone = models.CharField(max_length=15, verbose_name='شماره تماس')
    registration_date = models.DateField(verbose_name='تاریخ ثبت‌نام')
    monthly_fee = models.IntegerField(verbose_name='شهریه ماهانه (ریال)')
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='استاد'
    )

    class Meta:
        verbose_name = 'هنرجو'
        verbose_name_plural = 'هنرجویان'

    def __str__(self):
        return self.name


class ClassSession(models.Model):
    DAYS_OF_WEEK = [
        ('0', 'شنبه'),
        ('1', 'یکشنبه'),
        ('2', 'دوشنبه'),
        ('3', 'سه‌شنبه'),
        ('4', 'چهارشنبه'),
        ('5', 'پنجشنبه'),
        ('6', 'جمعه'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='هنرجو')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='استاد')
    day_of_week = models.CharField(max_length=1, choices=DAYS_OF_WEEK, verbose_name='روز هفته')
    time = models.TimeField(verbose_name='ساعت کلاس')

    class Meta:
        verbose_name = 'جلسه کلاس'
        verbose_name_plural = 'جلسات کلاس'

    def __str__(self):
        return f"{self.student.name} - {self.get_day_of_week_display()} {self.time}"


class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', 'حاضر'),
        ('absent', 'غایب'),
        ('makeup', 'جبرانی'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='هنرجو')
    class_session = models.ForeignKey(ClassSession, on_delete=models.CASCADE, verbose_name='جلسه کلاس')
    date = models.DateField(verbose_name='تاریخ')

    # جلسات ۱ تا ۵
    session_1 = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, verbose_name='جلسه ۱', blank=True)
    session_2 = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, verbose_name='جلسه ۲', blank=True)
    session_3 = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, verbose_name='جلسه ۳', blank=True)
    session_4 = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, verbose_name='جلسه ۴', blank=True)
    session_5 = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, verbose_name='جلسه ۵', blank=True)

    class Meta:
        verbose_name = 'حضور و غیاب'
        verbose_name_plural = 'حضور و غیاب‌ها'
        unique_together = ['student', 'date']

    def __str__(self):
        return f"{self.student.name} - {self.date}"

    def get_total_sessions(self):
        return 5

    def get_present_sessions(self):
        return sum([
            1 if self.session_1 == 'present' else 0,
            1 if self.session_2 == 'present' else 0,
            1 if self.session_3 == 'present' else 0,
            1 if self.session_4 == 'present' else 0,
            1 if self.session_5 == 'present' else 0,
        ])


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'نقدی'),
        ('card', 'کارت‌خوان'),
        ('transfer', 'انتقال بانکی'),
    ]

    for_year = models.IntegerField(
        verbose_name='سال آموزشی',
        default=1404,
        validators=[MinValueValidator(1400), MaxValueValidator(1500)]
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='هنرجو')
    amount = models.IntegerField(verbose_name='مبلغ پرداختی (ریال)')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, verbose_name='روش پرداخت')
    payment_date = models.DateField(verbose_name='تاریخ پرداخت')
    tracking_code = models.CharField(max_length=100, blank=True, verbose_name='کد پیگیری')
    for_month = PersianMonthField(verbose_name='برای ماه')
    teacher_share = models.IntegerField(default=0, verbose_name='سهم استاد (ریال)')

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت‌ها'

    def save(self, *args, **kwargs):
        if self.student.teacher:
            self.teacher_share = (self.amount * self.student.teacher.percentage_share) // 100
        else:
            self.teacher_share = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.amount} ریال"


class TeacherSettlement(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='استاد')
    amount = models.IntegerField(verbose_name='مبلغ تسویه (ریال)')
    settlement_date = models.DateField(verbose_name='تاریخ تسویه')
    description = models.TextField(blank=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'تسویه حساب استاد'
        verbose_name_plural = 'تسویه حساب با اساتید'

    def __str__(self):
        return f"{self.teacher.name} - {self.amount} ریال"


class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    issue_date = models.DateField(default=timezone.now)  
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
