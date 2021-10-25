from .database_postgrs import cursor,conn

cloumns_products='''
                product_name,
                id_part
                '''
cloumns_machines='''
                id
                '''

                
class Select_lists():
    def get_lest_items():
        product_list="SELECT %s FROM yt_parts_list ORDER BY product_name"%cloumns_products
        cursor.execute(product_list)
        git_data=cursor.fetchall()  
        data=[] 
        for item in git_data:
            #print(row)
            data.append(item[0])
        #print(data)
        return data
    def get_lest_machines():
        product_list="SELECT %s FROM yt_machine_list ORDER BY id"%cloumns_machines
        cursor.execute(product_list)
        git_data=cursor.fetchall()  
        data=[] 
        for item in git_data:
            #print(row)
            data.append(item[0])
        #print(data)
        return data
        #material by silo

class insert_value():
    pass

class Show_tables():
    
    def show_Load_machine():
        from_schema="SELECT * FROM yt_load_machine ORDER BY id"
        cursor.execute(from_schema)
        git_data=cursor.fetchall()  
        data=[] 
        for item in git_data:
            #print(row)
            data.append(item[0])
        print(data)
        return data
        #material by silo

class insert_value():
    pass