from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import additional_functions as add_f
from dotenv import load_dotenv


def main():
    dotenv.load_dotenv()
    excel_path = os.getenv("EXCEL_PATH")
    start_year = os.getenv("START_YEAR")

    years_since_inception = datetime.datetime.now().year - start_year
    form_year = add_f.get_form_word_year(years_since_inception)
    wines = add_f.get_exel_wine(excel_path)
    drink_groups = add_f.get_drink_groups(wines)
    add_f.change_index_html(years_since_inception, form_year, drink_groups)

    server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()