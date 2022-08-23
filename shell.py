from datetime import datetime, date

from my_app.models import *

owner = Owner.objects.create(fio='Sergey sergeyvich', data_sales='2022-08-09', status='Выкуп', block='1',
                             total_area='100')
owner_1 = Owner.objects.create(fio='Sergey Kakayto', data_sales='2021-11-09', status='Выкуп не до конца', block='2',
                               total_area='200')
owner_2 = Owner.objects.create(fio='Sergey Nishego', data_sales='2020-02-09', status='Расторгнуто', block='3',
                               total_area='300')
owner_3 = Owner.objects.create(fio='Sergey Crutoy', data_sales=('2019.03.09', '%Y-%m-%d'), status='Не продано', block='4', total_area='400', )

block1 = AllBlock.objects.create(number_block='100', cost_apart='100000', number_kol='100', floor_kol='1',
                                 num_apart_per_floor='10000')
block2 = AllBlock.objects.create(number_block='200', cost_apart='200000', number_kol='200', floor_kol='2',
                                 num_apart_per_floor='20000')
block3 = AllBlock.objects.create(number_block='400', cost_apart='300000', number_kol='300', floor_kol='3',
                                 num_apart_per_floor='30000')
block4 = AllBlock.objects.create(number_block='300', cost_apart='300000', number_kol='400', floor_kol='4',
                                 num_apart_per_floor='40000')
