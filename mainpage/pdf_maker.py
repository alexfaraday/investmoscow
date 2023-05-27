from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import random
import string

#
# def downlaod_pdf(request: HttpRequest): #Скачать pdf
#     image_3()
#     image_4()
#     make_pdf()
#     with open('mainpage/application/pdf/result.pdf', 'rb') as f:
#         file_data = f.read()
#
#     response = HttpResponse(file_data, content_type='application/pdf')
#     response['Content-Disposition'] = "attachment; filename=Result.pdf"
#     return response
#
#
# def image_3(path='mainpage/application/images/3.jpg'): #Здесь данные для 3 страницы
#     im = Image.open(path)
#     font = ImageFont.truetype("mainpage/font/Roboto-Regular.ttf", 64, encoding='UTF-8')
#     draw_text = ImageDraw.Draw(im)
#
#     branch = "Авиационная промышленность"
#     draw_text.text((1200, 560), branch, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     org_type = "ИП"
#     draw_text.text((1600, 770), org_type, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     employees_count = "{} человек".format(20)
#     draw_text.text((1500, 1120), employees_count, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     district = "ЦАО"
#     draw_text.text((1580, 1380), district, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     min_total_expenses = 100
#     max_total_expenses = 300
#     draw_text.text((1300, 1800), "От {} до {} млн.руб.".format(min_total_expenses, max_total_expenses),
#                    fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     employees_expenses = "{} млн.руб.".format(20)
#     draw_text.text((1500, 2190), employees_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     rent_expenses = "{} млн.руб.".format(140)
#     draw_text.text((1500, 2410), rent_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     taxes_expenses = "{} млн.руб.".format(20)
#     draw_text.text((1500, 2610), taxes_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     services_expenses = "{} млн.руб.".format(20)
#     draw_text.text((1500, 2800), services_expenses, fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     im.save('mainpage/application/images/3_1.jpg')
#
#
# def image_4(path='mainpage/application/images/4.jpg'): #Здесь данные для 4 страницы
#     im = Image.open(path)
#     font = ImageFont.truetype("mainpage/font/Roboto-Regular.ttf", 64, encoding='UTF-8')
#     draw_text = ImageDraw.Draw(im)
#
#     min_totals = 100
#     max_totals = 300
#     draw_text.text((1400, 1910), text="От {} до {} млн.руб.".format(min_totals, max_totals),
#                    fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     employees_count = 20
#     draw_text.text((1550, 2170), "{} человек ".format(employees_count), fill=('#1C0606'),
#                    font=font, stroke_width=1, stroke_fill="black")
#
#     min_pensionary_expenses = 10
#     max_pensionary_expenses = 100
#     draw_text.text((1400, 2430), "От {} до {} млн.руб. ".format(min_pensionary_expenses, max_pensionary_expenses),
#                    fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     min_health_expenses = 10
#     max_health_expenses = 100
#     draw_text.text((1400, 2700), "От {} до {} млн.руб. ".format(min_health_expenses, max_health_expenses),
#                    fill=('#1C0606'), font=font, stroke_width=1, stroke_fill="black")
#
#     im.save('mainpage/application/images/4_1.jpg')
#
#
# def make_pdf(): #Создание pdf
#     pdf = FPDF(format='A4')
#     pdf.add_page()
#     pdf.image('mainpage/application/images/1.jpg', x=0, y=0, w=211)
#     pdf.add_page()
#     pdf.image('mainpage/application/images/2.jpg', x=0, y=0, w=211)
#     pdf.add_page()
#     pdf.image('mainpage/application/images/3_1.jpg', x=0, y=0, w=211)
#     pdf.add_page()
#     pdf.image('mainpage/application/images/4_1.jpg', x=0, y=0, w=211)
#     pdf.output("mainpage/application/pdf/result.pdf")
#

def make_excel(branch,org_type,personal, district ): #Скачать excel

    #Первый лист
    branch = branch
    org_type = org_type
    employees_count =str(personal)+"{} человек".format(20)
    district = district
    organization_info = pd.DataFrame({'Наименование': ['Отрасль', 'Тип организации', 'Количество сотрудников',
                                                       'Район расположения производства'],
                                      'Значение': [branch, org_type, employees_count, district]})

    #Второй лист
    min_total_expenses = 100
    max_total_expenses = 300
    employees_expenses = "{} млн.руб.".format(20)
    rent_expenses = "{} млн.руб.".format(140)
    taxes_expenses = "{} млн.руб.".format(20)
    services_expenses = "{} млн.руб.".format(20)
    possible_costs = pd.DataFrame(
        {'Наименование': ['Персонал', 'Аренда объектов недвижимости',
                          'Налоги', 'Услуги', 'Итого возможных расходов'],
            'Значение': [employees_expenses, rent_expenses, taxes_expenses, services_expenses,
                         "От {} до {} млн.руб.".format(min_total_expenses, max_total_expenses)]})

    #Третий лист
    min_totals = 100
    max_totals = 300
    employees_count = 20
    min_pensionary_expenses = 10
    max_pensionary_expenses = 100
    min_health_expenses = 10
    max_health_expenses = 100
    organization_personal = pd.DataFrame(
        {'Наименование': ['Итого возможных расходов на содержание персонала организации',
                          'Планируемая численность персонала', 'Страховые взносы(пенсионное страхование)',
                          'Страховые взносы(медицинское страхование)'],
        'Значение': ["От {} до {} млн.руб.".format(min_totals, max_totals), "{} человек ".format(employees_count),
                     "От {} до {} млн.руб.".format(min_pensionary_expenses, max_pensionary_expenses),
                     "От {} до {} млн.руб.".format(min_health_expenses, max_health_expenses)]})
    letters = string.ascii_lowercase
    file_name=''.join(random.choice(letters) for i in range(10))

    writer = pd.ExcelWriter('/home/c/cp31594/django_gsvno/public_html/media/'+file_name+'result.xlsx', engine='xlsxwriter')

    #Названия листов
    info_sheets = {'Информация о вашей организации': organization_info,
                   'Итоговые возможные затраты': possible_costs,
                   'Персонал организации': organization_personal}

    #Заполнение excel
    for sheetname, df in info_sheets.items():
        df.to_excel(writer, sheet_name=sheetname, index=False)
        worksheet = writer.sheets[sheetname]
        for idx, col in enumerate(df):
            series = df[col]
            max_len = max(series.astype(str).map(len).max(), len(str(series.name))) + 10
            worksheet.set_column(idx, idx, max_len)
    writer.close()
    xxx=file_name+'result.xlsx'
    return xxx

    # with open('mainpage/application/ms-excel/result.xlsx', 'rb') as f:
    #     file_data = f.read()
    # response = HttpResponse(file_data, content_type='application/ms-excel')
    # response['Content-Disposition'] = "attachment; filename=Result.xlsx"
    #
    # return response