from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import Student, Teacher, Payment, ClassSession  


def home(request):
    pages = [
    {"name": "داشبورد", "url_name": "dashboard", "icon": "bi-speedometer2"},
    {"name": "گزارش ماهانه", "url_name": "monthly_report", "icon": "bi-file-text"},
    {"name": "حضور سریع", "url_name": "quick_attendance", "icon": "bi-clipboard-check"},
    {"name": "ادمین", "url_name": "admin:index", "icon": "bi-person-badge"}


]

    return render(request, "home.html", {"pages": pages})


def monthly_report(request):
    """
    نمایش صفحه گزارش‌گیری
    """
    if request.method == 'POST':
        try:
            year = int(request.POST.get('year'))
            month = int(request.POST.get('month'))
            return export_to_excel(year, month)
        except (ValueError, TypeError):
            return HttpResponse("خطا: سال و ماه باید به صورت عددی باشند")
    
    # لیست سال‌ها و ماه‌ها
    years = range(1400, 1410)
    months = [
        (1, 'فروردین'), (2, 'اردیبهشت'), (3, 'خرداد'),
        (4, 'تیر'), (5, 'مرداد'), (6, 'شهریور'),
        (7, 'مهر'), (8, 'آبان'), (9, 'آذر'),
        (10, 'دی'), (11, 'بهمن'), (12, 'اسفند')
    ]
    
    return render(request, 'monthly_report.html', {
        'years': years,
        'months': months
    })

def export_to_excel(year, month):
    """
    خروجی اکسل از گزارش ماهانه
    """
    # برای تست اولیه
    from django.http import HttpResponse
    import pandas as pd
    
    # داده‌های نمونه
    report_data = {
        'شاخص': ['کل درآمد', 'کل سهم اساتید', 'سود خالص'],
        'مبلغ (ریال)': [1000000, 300000, 700000]
    }
    
    df = pd.DataFrame(report_data)
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="گزارش_{month}_{year}.xlsx"'
    
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='گزارش مالی', index=False)
    
    return response

def dashboard(request):
    """
    داشبورد مدیریتی
    """
    # محاسبات آماری
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_income = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    
    
    recent_payments = Payment.objects.select_related('student').order_by('-payment_date')[:5]
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_income': total_income,
        'recent_payments': recent_payments,
    }
    
    return render(request, 'dashboard.html', context)


def calendar_view(request):
    classes = ClassSession.objects.all()
    events = []
    for class_obj in classes:
        events.append({
            'title': f"{class_obj.student.name} - {class_obj.teacher.name}",
            'start': f"2024-01-01T{class_obj.time}:00",  # dynamic date needed
            'color': '#d32f2f'
        })
    return render(request, 'calendar.html', {'events': events})

# در core/views.py
from django.shortcuts import render, redirect
from .models import Attendance, Student, ClassSession
from django.utils import timezone

def quick_attendance(request):
    """
    صفحه سریع برای ثبت حضور و غیاب
    """
    students = Student.objects.all()
    today = timezone.now().date()
    
    if request.method == 'POST':
        for student in students:
            # بررسی آیا رکورد برای امروز وجود دارد
            attendance, created = Attendance.objects.get_or_create(
                student=student,
                date=today,
                defaults={'class_session': student.classsession_set.first()}
            )
            
            # ثبت وضعیت هر جلسه
            for i in range(1, 6):
                field_name = f'session_{i}'
                status = request.POST.get(f'{student.id}_{i}', '')
                if status:
                    setattr(attendance, field_name, status)
            
            attendance.save()
        
        return redirect('admin:core_attendance_changelist')
    
    # دریافت وضعیت موجود برای امروز
    today_attendances = {}
    for student in students:
        try:
            att = Attendance.objects.get(student=student, date=today)
            today_attendances[student.id] = att
        except Attendance.DoesNotExist:
            today_attendances[student.id] = None
    
    context = {
        'students': students,
        'today': today,
        'today_attendances': today_attendances,
    }
    
    return render(request, 'admin/quick_attendance.html', context)