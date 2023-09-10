import datetime
from arconverter import arConverter


def test_convert_sttartofmonth_ok():
    result_one = arConverter.convert(datetime.datetime(2020, 2, 1, 0, 0, 0))
    assert result_one.year == 4720
    assert result_one.month == "Calistril"
    assert result_one.day == 1


def test_convert_endofmonth_ok():
    result_two = arConverter.convert(datetime.datetime(2020, 3, 31, 0, 0, 0))
    assert result_two.year == 4720
    assert result_two.month == "Pharast"
    assert result_two.day == 31
