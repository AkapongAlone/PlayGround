import pyodbc

conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  'AKAPONG\SQLEXPRESS'+'; DATABASE='+'MeasurLink'+';trusted_connection=yes;' )

con=conn.cursor()
data=[]
while True:
    con.execute(
                """SELECT distinct [StationName]
        
        ,CAST(ObsTimestamp AS DATE)
        ,[PartName]
        ,[FeatureName]
        
        
    FROM [MeasurLink].[dbo].[BigTable] """)

    datest = con.fetchone()
    if datest != None:
        
        data.append(datest)
        con.execute(
                    """;WITH CTE AS(SELECT  * FROM BigTable WHERE StationName=? AND CAST(ObsTimestamp AS DATE)=? AND [PartName]=? AND  [FeatureName]=? ) DELETE FROM CTE """, (datest[0],datest[1],datest[2], datest[3]))
    else:
        break
print(data)