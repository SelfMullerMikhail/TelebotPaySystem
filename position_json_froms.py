import json




class PositionJsonForms:
    def __init__(self) -> None:
        ...
        
    def get_json_order(self, position:str, position_id:str, price:int=0,
                    comment:str ="", size:str="M"): 
        order = {
                "position": f"{position}",
                "position_id": f"{position_id}",
                "price" : f"{price}",
                "size":f"{size}",
                "comment": f"{comment}",
                "additives": {}
                }
        return json.dumps(order)
    
    def get_json_additives(self, additives_id:str, additives_price:int=0):
        additive ={
            'position_id' : f'{additives_id}',
            'price': f'{additives_price}'
                } 
        return json.dumps(additive)