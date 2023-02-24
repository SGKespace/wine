from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import additional_functions as add_f


def main():
    year_of_creation = 1920
    years_since_inception = datetime.datetime.now().year - year_of_creation
    form_year = add_f.get_form_word_year(years_since_inception)
    wines = add_f.get_exel_wine('wine.xlsx')
    drink_groups = add_f.get_drink_groups(wines)
    add_f.change_index_html(years_since_inception, form_year, drink_groups)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()