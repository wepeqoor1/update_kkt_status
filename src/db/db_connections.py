import psycopg2


class Sql:

    def __init__(
            self,
            db_host: str,
            db_port: str,
            db_name: str,
            db_user: str,
            db_password: str
    ):
        self._connect_db = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        self._cursor = self._connect_db.cursor()

    def _select(self, request: str) -> list[tuple]:
        """
        На вход подается sql запрос
        На выходе массив построчно.
        :param request:
        :return row: list:
        """
        self._cursor.execute(request)
        return rows if (rows := self._cursor.fetchall()) else []

    def select(self, request: str) -> list[tuple]:
        result: list[tuple] = self._select(request)
        self._connect_db.rollback()
        return result

    def update(self, request: str) -> None:
        """
        На вход подается sql запрос
        :param request:
        """
        self._cursor.execute(request)
        self._connect_db.commit()
        self._connect_db.rollback()
