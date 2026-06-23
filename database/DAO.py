from database.DB_connect import DBConnect
from model.piazzamento import Piazzamento


class DAO():

    @staticmethod
    def getAllYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT year 
                        from seasons
                        order by year asc"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row['year'])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCircuits():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from circuits"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getPiazzamento(circuito, start, end):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select year, driverId, position
                    from results r, races r2 
                    where r.raceId = r2.raceId 
                    and circuitId = %s
                    and year >= %s
                    and year <= %s"""
        cursor.execute(query, (circuito, start, end))

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getArchi(start, end, mappa):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """with dettagli as(
                    select year, driverId, position, circuitId
                    from results r, races r2 
                    where r.raceId = r2.raceId 
                    and year >= %s
                    and year <= %s
                    and position is not null)
                    select d1.circuitId as c1, d2.circuitId as c2
                    from dettagli d1, dettagli d2
                    where d1.circuitId <> d2.circuitID
                    group by d1.circuitId, d2.circuitId"""
        cursor.execute(query, (start, end))

        res = []
        for row in cursor:
            res.append((mappa[row['c1']], mappa[row['c2']]))

        cursor.close()
        cnx.close()
        return res

