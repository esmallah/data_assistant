from .database_postgrs import cursor,conn
class Select_lists():
    def get_lest():
        product_list="SELECT product_name FROM yt_parts_list ORDER BY product_name"
        cursor.execute(product_list)
        git_data=cursor.fetchall()  
        data=[] 
        for row in git_data:
            #print(row)
            for item in row:
                data.append(item)
        #print(data)
        return data
        #material by silo
class insert_value():
    pass

