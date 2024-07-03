from database.DB_connect import DBConnect



class DAO():
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select distinct(year (s.`datetime`)) as anno
            from sighting s
            order by anno desc
        """
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(row["anno"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select id
            from state s 
        """
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append(row["id"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select *
            from neighbor n 
        """
        result = []
        cursor.execute(query)
        for row in cursor:
            result.append((row["state1"], row["state2"]))
        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getAllEdgesPeso(giorni, anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select n.state1, n.state2, s1.`datetime` as date1, s2.`datetime`as date2, count(distinct s1.id) + count(distinct s2.id) as peso
            from neighbor n, sighting s1, sighting s2
            where s1.id != s2.id 
                and s1.state = n.state1 and s2.state = n.state2
                and year(s1.`datetime`) = year(s2.`datetime`) and year(s1.`datetime`) = %s
                and datediff(s2.`datetime`, s1.`datetime`) <= %s
            group by n.state1, n.state2 
        """
        result = []
        cursor.execute(query, (anno, giorni, ))
        for row in cursor:
            result.append((row["state1"], row["state2"], row["peso"]))
        cursor.close()
        conn.close()
        return result






