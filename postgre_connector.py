import os
import psycopg2
import json
from dotenv import load_dotenv
from postgre_from import PostgreeForm

dotenv_path = os.path.join(os.path.dirname(__file__), '', 'env_file.env')
load_dotenv(dotenv_path=dotenv_path)




class PostGreeConnector:
    def __init__(self) -> None:
        self.__db_address = os.getenv("DB_ADDRESS")
        self.__database = os.getenv("DATA_BASE_NAME")
        self.__user = os.getenv("MY_USER_NAME_DB")
        self.__password = os.getenv("DB_PASSWORD")
        self.__port = os.getenv("DB_PORT")
    
    def __connect(self):
        conn = psycopg2.connect(
            host=self.__db_address,
            database=self.__database,
            user=self.__user,
            password=self.__password,
            port=self.__port 
            )
        return conn
    
    def __command_select(self, args) -> list:
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

    def __command_insert(self, args) -> None:
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
                        
    def select_all_from(self, from_:str, what:str="*"):
        if what != "*":
            what = f'"{what}"'
        info = self.__command_select(f'SELECT {what} FROM "{from_}";')
        return info

#  UserInfo--------------------------------------------------------------------
    
    def insert_UserInfo(self, user_id:int, user_name:str, 
                user_birthday:str='null', user_mail:str='null',
                user_discount:int='null', user_total_sum:int='null') -> None:
                            
        query = PostgreeForm(user_id).get_query_insert_UserInfo(user_name,
                user_birthday, user_mail, user_discount, user_total_sum)
        self.__command_insert(query) 
        return None

    def get_UserInfo(self, user_id:int):
        query = PostgreeForm(user_id).get_query_select_UserInfo()
        return self.__command_select(query)                
    
    def edit_UserInfo(self, table:str, set_name:str, set_param, where, what):
        query = PostgreeForm().get_query_edit_raw(table, set_name, set_param, 
                                                where, what)
        self.__command_insert(query)
        return None
# ProductOrder-----------------------------------------------------------------
    def create_order_position(self,user_id, position:str, position_id:str,
                            size:str="M"):
        id = self.__command_select(PostgreeForm(user_id).
                    get_query_count_orders ())[0][0]
        id = 1 if id is None else id + 1 
        json_form = PostgreeForm(user_id).get_json_order(position,
                                                        position_id, id)
        query = PostgreeForm(user_id).get_query_insert_order(id, 
                                                    json_form)
        self.__command_insert(query)
    
    def get_user_order(self, user_id):
        query = PostgreeForm(user_id,).get_query_info_order()
        info = self.__command_select(query)
        return info
    
    def insert_order_propertie(self, user_id:int, position_id:int, 
                            propertie:str, propertie_id:str,
                            propertie_price:int=0):
        
        properite_json = PostgreeForm().get_json_properties(
            propertie_id=propertie_id, propertie_price=propertie_price)
        query = PostgreeForm(user_id).get_query_insert_properie(propertie,
                                                position_id, properite_json)
        self.__command_insert(query)
        
    def create_order(self, user_id):
        query = PostgreeForm(user_id).get_query_create_order()
        self.__command_insert(query)

    
    

if __name__ == "__main__":
    bd = PostGreeConnector()
    # bd.insert_UserInfo(user_id=3, user_name="Lol", user_mail="p444g4@mail.ru")
    # bd.edit_UserInfo(table="UserInfo", set_name="user_name", set_param="Test4",
    #                 where="user_id", what=3)
    # info = bd.order_create_position(user_id = 3, position_id=1, position="Wino")
    # info = bd.select_all_from("UserInfo")
    # print(info)
    # info_position = bd.get_user_order(3)
    # bd.create_order(3)
    # ord = bd.create_order_position(user_id=3, position="Voda", 
    #                             position_id="trf3553gg3")
    bd.insert_order_propertie(user_id=3, position_id=1, propertie="Milk",
                            propertie_price=100, propertie_id=12)