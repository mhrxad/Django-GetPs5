from . import jalali
from django.utils import timezone


def jalali_date(time):
    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

    local_time = timezone.localtime(time)

    time_to_string = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_string).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(months):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    result = "{} {} {} , ساعت {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        local_time.hour,
        local_time.minute
    )

    return result


def gregorian_date(time):

    time_to_string = str(time)
    time_to_tuple = jalali.Persian(time_to_string).gregorian_tuple()
    time_to_list = list(time_to_tuple)

    return time_to_list
