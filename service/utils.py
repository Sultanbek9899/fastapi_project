def get_statistic_query(from_date, to_date, order_field):
    if all((from_date, to_date)):
        condition = f"WHERE date >= '{from_date}' AND date <= '{to_date}'"
    elif from_date and to_date is None:
        condition = f"WHERE date>='{from_date}'"
    elif from_date is None and to_date:
        condition = f"WHERE date>='{from_date}'"
    else:
        condition = ""
    query = f"""
        SELECT statistics.*, ROUND(statistics.cost/statistics.clicks, 2) as cpc, ROUND((cost/views * 1000), 2) as cpm  
        FROM statistics {condition} ORDER BY {order_field} DESC ;
        """
    return query
