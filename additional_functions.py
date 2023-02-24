from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import openpyxl
import collections
from collections import defaultdict
from pprint import pprint


def get_exel_wine_to_dict(file_xlsx):
    excel_data_df = pandas.read_excel(file_xlsx,  sheet_name='Лист1', keep_default_na=False)
    return excel_data_df.to_dict(orient='records')


def get_drink_groups(wines_dict):
    beverages_group = defaultdict(list)
    for beverage in wines_dict:
        beverages_group[beverage["Категория"]].append(beverage)
    # pprint(beverages_group)
    return beverages_group


def get_drink_groups_old(wines_dict):

    count_category = collections.Counter()
    for category in wines_dict:
        count_category[category['Категория']] += 1
    unique_category = list(count_category)

    beverages = {}
    for current_category in unique_category:
        for category in wines_dict:
            if category['Категория'] == current_category:
                try:
                    current = beverages[current_category]
                    beverages[current_category] = f'{current}, {category}'
                except KeyError:
                    beverages[current_category] = f'{category}'

        # beverages[current_category] = f'[{beverages[current_category].replace("nan","None")}]'
        beverages[current_category] = [f'{beverages[current_category].replace("nan", "None")}']
    pprint(beverages)
    return beverages


def change_index_html(years_since_inception, form_year, wines_dict):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years_since_inception=years_since_inception,
        form_year=form_year,
        wines=wines_dict
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def get_the_form_of_the_word_year(desired_year):
    if desired_year % 10 == 1 and desired_year != 11 and desired_year % 100 != 11:
        return 'год'
    elif 1 < desired_year % 10 <= 4 and desired_year != 12 and desired_year != 13 and desired_year != 14:
        return 'года'
    else:
        return 'лет'


def main():
    years_since_inception = datetime.datetime.now().year - 1920
    file_xlsx = 'wine3.xlsx'
    wines_dict = get_exel_wine_to_dict(file_xlsx)
    drink_groups = get_drink_groups(wines_dict)
    form_year = get_the_form_of_the_word_year(years_since_inception)
    change_index_html(years_since_inception, form_year, drink_groups)


if __name__ == '__main__':
    main()