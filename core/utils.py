from django.db.models import Sum
from .models import Payment, TeacherSettlement

def calculate_teacher_share(payment):
    """
    محاسبه سهم استاد از یک پرداخت
    """
    if payment.student.teacher:
        teacher_share = (payment.amount * payment.student.teacher.percentage_share) // 100
        return teacher_share
    return 0

def get_monthly_profit(year, month):
    """
    محاسبه سود ماهانه آموزشگاه
    """
    # کل پرداخت‌های وصول شده در ماه مشخص
    total_payments = Payment.objects.filter(
        for_month__year=year,
        for_month__month=month
    ).aggregate(total=Sum('amount'))['total'] or 0

    # کل سهم پرداخت شده به اساتید در ماه مشخص
    total_teacher_share = TeacherSettlement.objects.filter(
        settlement_date__year=year,
        settlement_date__month=month
    ).aggregate(total=Sum('amount'))['total'] or 0

    # سود آموزشگاه = کل پرداخت‌ها - کل سهم اساتید
    profit = total_payments - total_teacher_share
    return profit
from django.db.models import Sum
from django.http import HttpResponse
import pandas as pd
from .models import Payment, TeacherSettlement

def generate_monthly_report(year, month):
    """
    تولید گزارش کامل ماهانه
    """
    # داده‌ها را جمع‌آوری کنید
    payments = Payment.objects.filter(
        for_month__year=year,
        for_month__month=month
    )
    
    settlements = TeacherSettlement.objects.filter(
        settlement_date__year=year,
        settlement_date__month=month
    )
    
    # ایجاد DataFrame برای گزارش
    report_data = {
        'شاخص': ['کل درآمد', 'کل سهم اساتید', 'سود خالص'],
        'مبلغ (ریال)': [
            payments.aggregate(total=Sum('amount'))['total'] or 0,
            settlements.aggregate(total=Sum('amount'))['total'] or 0,
            (payments.aggregate(total=Sum('amount'))['total'] or 0) - 
            (settlements.aggregate(total=Sum('amount'))['total'] or 0)
        ]
    }
    
    df = pd.DataFrame(report_data)
    return df, f"گزارش {month}_{year}"

def export_to_excel(year, month):
    """
    خروجی اکسل از گزارش ماهانه
    """
    df, report_name = generate_monthly_report(year, month)
    
    # ایجاد response برای دانلود فایل اکسل
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{report_name}.xlsx"'
    
    # ذخیره در response
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='گزارش مالی', index=False)
        
        # sheet دوم: پرداخت‌ها
        payments = Payment.objects.filter(
            for_month__year=year,
            for_month__month=month
        ).values('student__name', 'amount', 'payment_method', 'payment_date')
        pd.DataFrame(payments).to_excel(writer, sheet_name='پرداخت‌ها', index=False)
    
    return response