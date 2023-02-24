from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import openpyxl
import collections
from collections import defaultdict


def get_exel_wine(file_xlsx):
    excel_data_df = pandas.read_excel(file_xlsx,  sheet_name='Лист1', keep_default_na=False)
    return excel_data_df.to_dict(orient='records')


def get_drink_groups(wines):
    beverages_group = defaultdict(list)
    for beverage in wines:
        beverages_group[beverage["Категория"]].append(beverage)
    return beverages_group


def change_index_html(years_since_inception, form_year, wines):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        years_since_inception=years_since_inception,
        form_year=form_year,
        wines=wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def get_form_word_year(desired_year):
    if desired_year % 10 == 1 and desired_year != 11 and desired_year % 100 != 11:
        return 'год'
    elif 1 < desired_year % 10 <= 4 and desired_year != 12 and desired_year != 13 and desired_year != 14:
        return 'года'
    else:
        return 'лет'


def main():
    year_of_creation = 1920
    years_since_inception = datetime.datetime.now().year - year_of_creation
    file_xlsx = 'wine.xlsx'
    wines = get_exel_wine(file_xlsx)
    drink_groups = get_drink_groups(wines)
    form_year = get_form_word_year(years_since_inception)
    change_index_html(years_since_inception, form_year, drink_groups)


if __name__ == '__main__':
    main()