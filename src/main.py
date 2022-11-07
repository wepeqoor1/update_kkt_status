import os

from dotenv import load_dotenv

from src.db.db_connections import Sql
from src.db.sql_request_patterns import kkt_activated_true


def main():
    load_dotenv()
    db_host = os.getenv('DB_PROM_HOST')
    db_port = os.getenv('DB_PROM_PORT')
    db_name = os.getenv('DB_PROM_NAME')
    db_user = os.getenv('DB_PROM_LOGIN')
    db_password = os.getenv('DB_PROM_PASSWORD')

    sql = Sql(db_host, db_port, db_name, db_user, db_password)

    kkts_status = sql.select(kkt_activated_true)
    print(kkts_status)
    # current_kkt_status = get_current_kkt_status(kkt_status)
    # write_to_file()


if __name__ == '__main__':
    main()
