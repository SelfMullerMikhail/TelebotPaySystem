import json

class PostgreeForm:
    def __init__(self, user_id:int=None) -> None:
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
        
        self.user_id, user_name, user_birthday, user_mail, user_discount, \
        user_total_sum = (
        self.__null_detected(self.user_id, user_name, user_birthday, user_mail,
                                            user_discount, user_total_sum))
        info = f"""
            INSERT INTO "UserInfo" (user_id, user_name, user_birthday,
                user_mail, user_discount, user_total_summ) 
            VALUES ({self.user_id}, {user_name}, {user_birthday}, {user_mail},
                {user_discount}, {user_total_sum});"""
        return info
    
    def get_query_edit_raw(self, table:str, set_name:str,
                                                    set_param, where, what):
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
    
    def get_json_order(self, position:str, position_id:str, price:int=0,
                    comment:str ="", size:str="M"): 
        order = {
                "position": f"{position}",
                "position_id": f"{position_id}",
                "price" : f"{price}",
                "size":f"{size}",
                "comment": f"{comment}",
                "properties": json.dumps({})
                }
        return json.dumps(order)
    
    
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
    
    # def get_query_insert_firtht_order():
    #     id = self.__shielding(id)
    #     query = f"""INSERT INTO "ProductOrder"
    #                 , 
    #                 '{json_form}')
    #                 WHERE user_id = {self.user_id};"""
    #     return query
    
    def get_query_select_UserInfo(self):
        query = f"""SELECT "order_info" 
                FROM "ProductOrder" 
                WHERE user_id = {self.user_id};"""
        return query

    def get_json_properties(self, propertie_id:str, propertie_price:int=0):
        proper ={
            'position_id' : f'{propertie_id}',
            'price': f'{propertie_price}'
                } 
        return json.dumps(proper)
    
    def get_query_insert_properie(self, propertie:str, position_id:int, 
                                json_form:json):
        propertie = self.__shielding(propertie)
        query = f"""UPDATE "ProductOrder"
            SET order_info = jsonb_insert(order_info -> '{position_id}' -> properties,
            {propertie}, '{json_form}')
            WHERE user_id = {self.user_id};"""
        return query
        

if __name__ == "__main__":
    ...
    