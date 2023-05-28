#!/usr/bin/env python
# coding: utf-8

# In[8]:


def rent(square: int, district: int, type: int, special_zone: bool) -> dict:
    '''
    Функция расчета аренды, аренда+ ремонт, аренда+строительство, покупка, покупка+ремонт
    На вход принимается площадь,округ, тип реализации проека, проверка ОЭЗ(особая экономическая зона).
    Эти данные вводит пользователь.
    Выходные данные формируются в словарь.
    '''

    dict_district = {1: 657.86,  # ЦАО
                     2: 1164.55,  # САО
                     3: 697.97,  # СВАО
                     4: 1064.41,  # ВАО
                     5: 948.40,  # ЮВАО
                     6: 898.01,  # ЮАО
                     7: 1841.33,  # ЮЗАО
                     8: 776.76,  # ЗАО
                     9: 600.00,  # СЗАО
                     10: 803.99,  # ЗелАО
                     11: 670.33,  # ТАО
                     12: 685.53}  # НАО
    dict_district_buy = {1: 143790.10,  # ЦАО
                         2: 89873.67,  # САО
                         3: 96446.17,  # СВАО
                         4: 59288.15,  # ВАО
                         5: 75014.48,  # ЮВАО
                         6: 88668.48,  # ЮАО
                         7: 78868.48,  # ЮЗАО
                         8: 53327.22,  # ЗАО
                         9: 117696.30,  # СЗАО
                         10: 70926.20,  # ЗелАО
                         11: 9285.50,  # ТАО
                         12: 78000}  # НАО
    dict_kadastr = {1: 63274.79,  # ЦАО
                    2: 20532.99,  # САО
                    3: 19485.33,  # СВАО
                    4: 15492.36,  # ВАО
                    5: 14086.97,  # ЮВАО
                    6: 13510.37,  # ЮАО
                    7: 16423.10,  # ЮЗАО
                    8: 11703.22,  # ЗАО
                    9: 19961.59,  # СЗАО
                    10: 4111.50,  # ЗелАО
                    11: 2890.51,  # ТАО
                    12: 5333.94}  # НАО
    dict_sz_rent = {4: 712.5,  # ВАО
                    10: 916.66,  # ЗелАО
                    5: 1012.50}  # ЮВАО

    district_of_special_zone_index = [4, 10, 5]  # ВАО,ЗелАО,ЮВАО
    period = [6, 12]
    cost_of_capital_construction = [80_000, 120_000]
    repair = 5000

    if special_zone:
        if type > 3 or district not in district_of_special_zone_index:
            return "Введены некорректные данные"
        else:
            if type == 2 and district_of_special_zone_index[0] == 1:  # Аренда
                amount_of_rent_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0]
                amount_of_rent_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1]
                res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_sz_6,
                            'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_sz_12}
                return res_dict
            elif type == 1 and district_of_special_zone_index[0] == 1:  # Аренда+ремонт
                amount_of_rent_repair_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0] + (repair * square)
                amount_of_rent_repair_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1] + (repair * square)
                res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_sz_6,
                            'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_sz_12}
                return res_dict
            elif type == 3 and district_of_special_zone_index[0] == 1:  # Аренда+строительство
                amount_of_rent_build_sz_6 = [round(dict_sz_rent[district] * square, 3) * period[0] + i for i in
                                             list(map(lambda x: x * square, cost_of_capital_construction))]
                amount_of_rent_build_sz_12 = [round(dict_sz_rent[district] * square, 3) * period[1] + i for i in
                                              list(map(lambda x: x * square, cost_of_capital_construction))]
                res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_sz_6,
                            'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_sz_12}
                return res_dict
            elif type == 2 and district_of_special_zone_index[1] == 3:  # Аренда
                amount_of_rent_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0]
                amount_of_rent_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1]
                res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_sz_6,
                            'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_sz_12}
                return res_dict
            elif type == 1 and district_of_special_zone_index[1] == 3:  # Аренда+ремонт
                amount_of_rent_repair_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0] + (repair * square)
                amount_of_rent_repair_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1] + (repair * square)
                res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_sz_6,
                            'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_sz_12}
                return res_dict
            elif type == 3 and district_of_special_zone_index[1] == 3:  # Аренда+строительство
                amount_of_rent_build_sz_6 = [round(dict_sz_rent[district] * square, 3) * period[0] + i for i in
                                             list(map(lambda x: x * square, cost_of_capital_construction))]
                amount_of_rent_build_sz_12 = [round(dict_sz_rent[district] * square, 3) * period[1] + i for i in
                                              list(map(lambda x: x * square, cost_of_capital_construction))]
                res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_sz_6,
                            'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_sz_12}
                return res_dict
            elif type == 2 and district_of_special_zone_index[2] == 11:  # Аренда
                amount_of_rent_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0]
                amount_of_rent_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1]
                res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_sz_6,
                            'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_sz_12}
                return res_dict
            elif type == 1 and district_of_special_zone_index[2] == 11:  # Аренда+ремонт
                amount_of_rent_repair_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0] + (repair * square)
                amount_of_rent_repair_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1] + (repair * square)
                res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_sz_6,
                            'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_sz_12}
                return res_dict
            elif type == 3 and district_of_special_zone_index[2] == 11:  # Аренда+строительство
                amount_of_rent_build_sz_6 = [round(dict_sz_rent[district] * square, 3) * period[0] + i for i in
                                             list(map(lambda x: x * square, cost_of_capital_construction))]
                amount_of_rent_build_sz_12 = [round(dict_sz_rent[district] * square, 3) * period[1] + i for i in
                                              list(map(lambda x: x * square, cost_of_capital_construction))]
                res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_sz_6,
                            'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_sz_12}
                return res_dict

    else:
        if type == 2:  # Аренда
            amount_of_rent_perdistrict_6 = round(dict_district[district] * square, 3) * period[0]  # Аренда за 6 месяцев
            amount_of_rent_perdistrict_12 = round(dict_district[district] * square, 3) * period[1]  # Арена за 12 месцев
            res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_perdistrict_6,
                        'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_perdistrict_12}
            return res_dict
        elif type == 1:  # Аренда + ремонт
            amount_of_rent_repair_6 = round(dict_district[district] * square, 3) * period[0] + (repair * square)
            amount_of_rent_repair_12 = round(dict_district[district] * square, 3) * period[1] + (repair * square)
            res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_6,
                        'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_12}
            return res_dict
        elif type == 3:  # Аренда+строительство
            amount_of_rent_build_6 = [round(dict_district[district] * square, 3) * period[0] + i for i in
                                      list(map(lambda x: x * square, cost_of_capital_construction))]
            amount_of_rent_build_12 = [round(dict_district[district] * square, 3) * period[1] + i for i in
                                       list(map(lambda x: x * square, cost_of_capital_construction))]
            res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_6,
                        'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_12}
            return res_dict
        elif type == 4:  # Покупка
            amount_of_buy = round(dict_district_buy[district] * square, 3) + (dict_kadastr[district] * square) * 1.9 + (
                        dict_kadastr[
                            district] * square) * 1.5  # покупка+ сумма налога на имущество за год + сумма налога на землю за год
            res_dict = {'Покупка здания(ремонт не требуется)': amount_of_buy}
            return res_dict
        elif type == 5:  # Покупка + ремонт
            amount_of_buy_repair = round(dict_district_buy[district] * square, 3) + (
                        dict_kadastr[district] * square) * 1.9 + (
                                               dict_kadastr[district] * square) * 1.5 + repair * square
            res_dict = {'Покупка здания(ремонт требуется)': amount_of_buy_repair}
            return res_dict

    #print('Введены некорректные данные')

# In[10]:


# rent(square=100, district=1, type=1, special_zone=False)

