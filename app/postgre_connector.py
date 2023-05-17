import os

import psycopg2
from position_json_froms import PositionJsonForms
from postgre_from import PostgreeForm


class PostGreeConnector:
    def __init__(self) -> None:
        self.__db_address = os.getenv("DB_ADDRESS")
        self.__database = os.getenv("DATA_BASE_NAME")
        self.__user = os.getenv("MY_USER_NAME_DB")
        self.__password = os.getenv("DB_PASSWORD")
        self.__port = os.getenv("DB_PORT")

    def __connect(self):
        return (psycopg2.connect(
            host=self.__db_address, database=self.__database, user=self.__user,
            password=self.__password, port=self.__port))

    def __command_select(self, args: str) -> list:
        try:
            with self.__connect() as conn:
                cur = conn.cursor()
                cur.execute(args)
                info = cur.fetchall()
            return info
        except Exception as e:
            raise Exception(f"PostGreeConnector.select: {args}") from e
        finally:
            cur.close()

    def __command_insert(self, args: str) -> None:
        try:
            with self.__connect() as conn:
                cur = conn.cursor()
                cur.execute(args)
                conn.commit
                conn.commit()
        except Exception as e:
            raise Exception(f"PostGreeConnector.select: {args}") from e
        finally:
            cur.close()

    def select_all_from(self, from_: str, what: str = "*") -> str:
        if what != "*":
            what = f'"{what}"'
        info = self.__command_select(f'SELECT {what} FROM "{from_}";')
        return info

#  UserInfo--------------------------------------------------------------------

    def create_UserInfo(self, user_id: int, user_name: str,
                        user_birthday: str = 'null', user_mail: str = 'null',
                        user_discount: int = 'null',
                        user_total_sum: int = 'null') -> None:

        query = PostgreeForm(user_id).get_query_insert_UserInfo(user_name,
                                                                user_birthday,
                                                                user_mail,
                                                                user_discount,
                                                                user_total_sum)
        self.__command_insert(query)
        return None

    def get_UserInfo(self, user_id: int) -> list:
        query = PostgreeForm(user_id).get_query_select_UserInfo()
        return self.__command_select(query)

    def edit_UserInfo(self, table: str, set_name: str, set_param, where, what):
        query = PostgreeForm().get_query_edit_raw(table, set_name, set_param,
                                                  where, what)
        self.__command_insert(query)
        return None

# ProductOrder-----------------------------------------------------------------

    def create_order(self, user_id):
        query = PostgreeForm(user_id).get_query_create_order()
        self.__command_insert(query)

    def create_order_position(self, user_id, position: str, position_id: str,
                              size: str = "M"):
        size = size
        id = self.__command_select(PostgreeForm(user_id).
                                   get_query_count_orders())[0][0]
        id = 1 if id is None else id + 1
        json_form = PositionJsonForms().get_json_order(position,
                                                       position_id, id)
        query = PostgreeForm(user_id).get_query_insert_order(id,
                                                             json_form)
        self.__command_insert(query)

    def get_user_order(self, user_id):
        query = PostgreeForm(user_id,).get_query_info_order()
        info = self.__command_select(query)
        return info

    def delete_user_position(self, user_id: int, position_id: int) -> None:
        query = PostgreeForm(user_id=user_id).get_query_delete_order(
                                                                position_id)
        self.__command_insert(query)

    def clear_bascket(self, user_id):
        query = PostgreeForm(user_id).get_query_clear_bascket()
        self.__command_insert(query)

# ProductOrder-additives------------------------------------------------------

    def create_order_additives(self, user_id: int, position_id: int,
                               additives: str, additives_id: str,
                               additives_price: int = 0):

        json_form_additives = PositionJsonForms().get_json_additives(
            additives_id=additives_id, additives_price=additives_price)
        query = (PostgreeForm(user_id).
                 get_query_insert_additives(additives, position_id,
                                            json_form_additives))
        self.__command_insert(query)

    def delete_position_additives(self, user_id, position_id, additives
                                  ) -> None:
        query = PostgreeForm(user_id).get_query_delete_additives(position_id,
                                                                 additives)
        self.__command_insert(query)

    def get_position_additives(self, user_id, position_id) -> dict:
        query = PostgreeForm(user_id).get_query_get_additives(position_id)
        result = self.__command_select(query)
        if result == []:
            return None
        return result[0][0]

    def move_pay_transaction(self, user_id):
        query = PostgreeForm(user_id).get_query_pay_transaction()
        self.__command_insert(query)


if __name__ == "__main__":
    bd = PostGreeConnector()
    bd.create_UserInfo()
    bd.get_UserInfo()
    bd.edit_UserInfo()

    bd.create_order()
    bd.create_order_position()
    bd.get_user_order()
    bd.delete_user_position()
    bd.clear_bascket()

    bd.create_order_additives()
    bd.delete_position_additives()
    bd.get_position_additives()

    bd.move_pay_transaction()
