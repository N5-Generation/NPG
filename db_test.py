import psycopg2


def service_details():
    con = psycopg2.connect(service='example')
    cur = con.cursor()
    cur.execute('select version() as version '
                ', current_database() as db '
                ', current_user as user '
                ', now()::text as query_time '
                )
    result = cur.fetchone()
    return result

if __name__ == '__main__':
    x = service_details()
    print(x)