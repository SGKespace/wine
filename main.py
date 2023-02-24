from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import additional_functions as add_f


def main():
    years_since_inception = datetime.datetime.now().year - 1920
    form_year = add_f.get_the_form_of_the_word_year(years_since_inception)
    wines_dict = add_f.get_exel_wine_to_dict('wine.xlsx')
    drink_groups = add_f.get_drink_groups(wines_dict)
    add_f.change_index_html(years_since_inception, form_year, drink_groups)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()