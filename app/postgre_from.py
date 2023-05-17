import json


class PostgreeForm:
    def __init__(self, user_id: int = None) -> None:
        self.user_id = user_id

    def __null_detected(self, *arg):
        pparam = [f"'{obj}'" if isinstance(obj, str) and obj != 'null' else
                  obj for obj in arg]
        return pparam

    def __shielding(self, id):
        id = f"<<{id}>>".replace("<<", "'{")
        id = id.replace(">>", "}'")
        return id

    def get_query_insert_UserInfo(self, user_name, user_birthday, user_mail,
                                  user_discount, user_total_sum):

        self.user_id, user_name, user_birthday, user_mail, user_discount,
        user_total_sum = (self.__null_detected(self.user_id, user_name,
                                               user_birthday, user_mail,
                                               user_discount, user_total_sum))
        info = f"""
            INSERT INTO "UserInfo" (user_id, user_name, user_birthday,
                user_mail, user_discount, user_total_summ)
            VALUES ({self.user_id}, {user_name}, {user_birthday}, {user_mail},
                {user_discount}, {user_total_sum});"""
        return info

    def get_query_edit_raw(self, table: str, set_name: str, set_param, where,
                           what):
        what, set_param = self.__null_detected(what, set_param)
        info = f"""UPDATE "{table}"
                SET "{set_name}" = {set_param}
                WHERE {where} = {what};"""
        return info

    def get_query_info_order(self):
        query = f"""SELECT "order_info"
                    FROM "ProductOrder"
                    WHERE user_id = {self.user_id};"""
        return query

    def get_query_count_orders(self):
        query = f"""SELECT MAX(CAST(key AS INTEGER))
                    FROM jsonb_object_keys((SELECT order_info
                    FROM "ProductOrder"
                    WHERE user_id={self.user_id})::jsonb) key;"""
        return query

    def get_query_insert_order(self, id, json_form):
        id = self.__shielding(id)
        query = f"""UPDATE "ProductOrder"
                    SET order_info = jsonb_insert(order_info, {id},
                    '{json_form}'::jsonb)
                    WHERE user_id = {self.user_id};"""
        return query

    def get_query_create_order(self):
        query = f"""INSERT INTO "ProductOrder"(user_id)
                    VALUES({self.user_id})"""
        return query

    def get_query_select_UserInfo(self):
        query = f"""SELECT "order_info"
                FROM "ProductOrder"
                WHERE user_id = {self.user_id};"""
        return query

    def get_query_insert_additives(self, additives: str, position_id: int,
                                   json_form_additives: json):
        form = self.__shielding(f'{position_id},additives,{additives}')
        query = f"""UPDATE "ProductOrder"
                    SET order_info = jsonb_insert(
                    order_info,
                    {form},
                    '{json_form_additives}'
                    ); """
        return query

    def get_query_delete_additives(self, position_id, additives):
        json_form = self.__shielding(f'{position_id}, additives ,{additives}')
        query = f"""UPDATE "ProductOrder"
        SET order_info = order_info #- {json_form}
        WHERE user_id = {self.user_id};"""
        return query

    def get_query_get_additives(self, position_id):
        query = f"""
                SELECT jsonb_extract_path_text(jsonb_build_object('data',
                order_info), 'data', '{position_id}', 'additives')
                FROM "ProductOrder" WHERE user_id = {self.user_id};
                """
        return query

    def get_query_delete_order(self, order_id):
        query = f"""
                UPDATE "ProductOrder"
                SET order_info = order_info - '{order_id}'
                WHERE user_id = {self.user_id};
                """
        return query

    def get_query_clear_bascket(self):
        query = f"""
                UPDATE "ProductOrder"
                SET order_info = '{json.dumps({})}'
                WHERE user_id ={self.user_id};
        """
        return query

    def get_query_pay_transaction(self):
        query = f"""
                BEGIN;
                INSERT INTO "ProductHistory" (user_id, order_info)
                SELECT user_id, order_info
                FROM "ProductOrder"
                WHERE user_id = {self.user_id};
                DELETE FROM "ProductOrder" WHERE user_id = 3;
                COMMIT;
                """
        return query
