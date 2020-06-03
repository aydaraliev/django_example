import pandas as pd
import numpy as np
import ast
from django_pandas.io import read_frame

'''test = Orders.objects.all()
df = read_frame(test)
print(df.to_html())


def test_function(zakazy):
    zakazy = zakazy.objects.all()
    df = read_frame(zakazy)
    return df.to_html()'''


def convert_time_orders(orders):
    orders.delivered_at = pd.to_datetime(orders.delivered_at) + pd.Timedelta(3, 'h')  # utc = True
    orders.cooked_at = pd.to_datetime(orders.cooked_at) + pd.Timedelta(3, 'h')
    orders.taken_at = pd.to_datetime(orders.taken_at) + pd.Timedelta(3, 'h')
    orders.payed_at = pd.to_datetime(orders.payed_at) + pd.Timedelta(3, 'h')


def split_by_interval(table, column, period='M'):
    splitted_list = [g for n, g in table.set_index(column).groupby(pd.Grouper(freq=period))]
    return splitted_list


def create_basket(orders):
    basket = orders.basket[orders.basket.notnull()]
    mega_basket = np.array([])
    for i, v in basket.iteritems():
        mega_basket = np.append(mega_basket, ast.literal_eval(v))
    mega_basket = pd.Series(mega_basket.astype(int))
    mega_basket = mega_basket.value_counts()
    # удаляем левый id
    if 76669 in mega_basket.index:
        mega_basket = mega_basket.drop([76669])

    return mega_basket


def calc_dish_prices(basket, item_prices):
    dish_prices = item_prices[item_prices.id.isin(basket.index)]
    dish_prices = dish_prices.set_index('id')
    dish_prices = dish_prices[['price', 'meta_item_id']]
    return dish_prices


def concat_basket_prices(basket, dish_prices):
    basket_with_prices = pd.concat([basket, dish_prices], axis=1)
    basket_with_prices = basket_with_prices.sort_values(0, ascending=False)
    basket_with_prices.columns = ['n_orders', 'price', 'meta_item_id']
    basket_with_prices['total_money'] = basket_with_prices['n_orders'] * basket_with_prices['price']
    basket_with_prices = basket_with_prices[basket_with_prices.total_money.notnull()]
    basket_with_prices['meta_item_id'] = basket_with_prices.meta_item_id.astype(int)
    basket_with_prices.index.name = 'price_id'
    basket_with_prices.set_index('meta_item_id', append=True, inplace=True)
    basket_with_prices = basket_with_prices.swaplevel(0, 1)

    return basket_with_prices


def calc_sum(basket_with_prices):
    basket_with_prices = basket_with_prices.groupby(level='meta_item_id')
    basket_with_prices = basket_with_prices['n_orders', 'total_money'].agg({'n_orders': 'sum', 'total_money': 'sum'})
    price = basket_with_prices.total_money / basket_with_prices.n_orders
    basket_with_prices['price'] = price

    return basket_with_prices


def add_dish_names(basket_with_prices, item_names):
    dish_names = item_names[item_names.id.isin(basket_with_prices.index)]
    dish_names = dish_names.set_index('id')
    dish_names = dish_names['title']
    # соединяем
    basket_names_and_prices = pd.concat([basket_with_prices, dish_names], axis=1)

    return basket_names_and_prices


def brush_table(money_orders_names):
    money_orders_names.sort_values('total_money', ascending=False, inplace=True)
    money_orders_names.reset_index(inplace=True)
    money_orders_names.rename(columns={"index": "meta_item_id"}, inplace=True)


def orders_amount_by_interval(orders, interval):
    orders_by_months = split_by_interval(orders, 'payed_at', interval)
    orders_amount_bi = []
    # месяц это интервал, может быть днем, может быть неделей итп
    for month in orders_by_months:
        if month.empty:
            print('propuskaem interval')
        else:
            mega_basket = create_basket(month)
            dish_prices = calc_dish_prices(mega_basket, item_prices)
            basket_with_prices = concat_basket_prices(mega_basket, dish_prices)
            money_orders = calc_sum(basket_with_prices)
            money_orders_names = add_dish_names(money_orders, item_names)
            '''индексы, добавить на потом.
            money_orders_names = money_orders_names.set_index('date', append=True).swaplevel(0,1)
            индекы'''
            brush_table(money_orders_names)
            # добавляем столбец с датой
            date = np.full(money_orders_names.shape[0], month.index[0].to_period(interval))
            date = pd.Series(date)
            money_orders_names['date'] = date

        orders_amount_bi.append(money_orders_names)

    return orders_amount_bi


def split_by_kitchen(orders):
    orders_sorted_by_kitchen = orders.sort_values('kitchen_id')
    by_kitchen = [orders_sorted_by_kitchen[orders_sorted_by_kitchen.kitchen_id == x].reset_index(drop=True) for x in
                  orders_sorted_by_kitchen.kitchen_id.unique()]

    return by_kitchen


def get_results_by_kitchen(orders, intervals):
    kitchens = split_by_kitchen(orders)
    for interval in intervals:
        for kitchen in kitchens:
            kitchen_name = './orders_by_kitchen/' + str(kitchen.kitchen_id[0]) + '_' + interval + '_' + '_kuhnya.csv'
            kitchen_interval_list = orders_amount_by_interval(kitchen, interval)
            kitchen_interval_money_orders_names = pd.concat(kitchen_interval_list[::-1])
            kitchen_interval_money_orders_names.to_csv(kitchen_name, sep='\t', index=False)


def common_report(orders, item_prices, item_names, report_type, download=None):  # , item_names, interval='M'):
    # парсим заказы
    orders = orders.objects.all()
    orders = read_frame(orders)
    orders = orders.reset_index(drop=True)
    convert_time_orders(orders)
    # --------------------------------------
    # парсим цены
    item_prices = item_prices.objects.all()
    item_prices = read_frame(item_prices)
    item_prices = item_prices.reset_index(drop=True)
    # --------------------------------------
    # парсим названия блюд
    item_names = item_names.objects.all()
    item_names = read_frame(item_names)
    item_names = item_names.reset_index(drop=True)

    def create_report(orders, item_prices, item_names, report_type, download=None):
        basket = orders.basket[orders.basket.notnull()]
        basket = basket.astype('str')
        mega_basket = np.array([])
        for i, v in basket.iteritems():
            mega_basket = np.append(mega_basket, ast.literal_eval(v))
        mega_basket = pd.Series(mega_basket.astype(int))
        mega_basket = mega_basket.value_counts()
        # удаляем левый id
        if 76669 in mega_basket.index:
            mega_basket = mega_basket.drop([76669])

        dish_prices = calc_dish_prices(mega_basket, item_prices)
        basket_with_prices = concat_basket_prices(mega_basket, dish_prices)
        money_orders = calc_sum(basket_with_prices)
        money_orders_names = add_dish_names(money_orders, item_names)
        brush_table(money_orders_names)

        if report_type in ['D', 'W', 'M']:
            date = np.full(money_orders_names.shape[0], day.index[0].to_period(report_type))
            date = pd.Series(date)
            money_orders_names['date'] = date

        return money_orders_names

    if report_type == 'D':
        orders_by_days = split_by_interval(orders, 'payed_at', report_type)
        days = []
        for day in orders_by_days:
            if day.empty:
                pass
            else:
                day = create_report(day, item_prices, item_names, report_type)
                days.append(day)
        days = pd.concat(days[::-1])
        if download is None:
            return days.to_html()
        else:
            return days.to_csv(sep='\t')

    if report_type == 'W':
        orders_by_days = split_by_interval(orders, 'payed_at', report_type)
        days = []
        for day in orders_by_days:
            if day.empty:
                pass
            else:
                day = create_report(day, item_prices, item_names, report_type)
                days.append(day)
        days = pd.concat(days[::-1])
        if download is None:
            return days.to_html()
        else:
            return days.to_csv(sep='\t')

    if report_type == 'M':
        orders_by_days = split_by_interval(orders, 'payed_at', report_type)
        days = []
        for day in orders_by_days:
            if day.empty:
                pass
            else:
                day = create_report(day, item_prices, item_names, report_type)
                days.append(day)
        days = pd.concat(days[::-1])
        if download is None:
            return days.to_html()
        else:
            return days.to_csv(sep='\t')

    if report_type == 'A':
        report = create_report(orders, item_prices, item_names, report_type)
        if download is None:
            return report.to_html()
        else:
            return report.to_csv(sep='\t')

    return money_orders_names.to_html()


if __name__ == '__main__':
    orders = pd.read_csv('kitchen_production_public_orders.csv')
    item_names = pd.read_csv('kitchen_production_public_meta_items.csv')
    item_prices = pd.read_csv('kitchen_production_public_items.csv')

    convert_time_orders(orders)

    # все заказы
    mega_basket = create_basket(orders)
    dish_prices = calc_dish_prices(mega_basket, item_prices)
    basket_with_prices = concat_basket_prices(mega_basket, dish_prices)
    money_orders = calc_sum(basket_with_prices)
    money_orders_names = add_dish_names(money_orders, item_names)
    brush_table(money_orders_names)
    money_orders_names.to_csv('n_orders_money_dishes.csv', sep='\t', index=False)
    # заказы по месяцам/неделям и.т.п
    interval_list = orders_amount_by_interval(orders, 'W')
    interval_money_orders_names = pd.concat(interval_list[::-1])
    interval_money_orders_names.to_csv('interval_n_orders_money_dishes.csv', sep='\t', index=False)
    # заказы по кухням
    '''kitchens = split_by_kitchen(orders)
    for kitchen in kitchens:
        kitchen_name = './orders_by_kitchen/'+str(kitchen.kitchen_id[0])+'_kuhnya.html'
        print(kitchen_name)
        kitchen_interval_list = orders_amount_by_interval(kitchen, 'M')
        kitchen_interval_money_orders_names = pd.concat(kitchen_interval_list[::-1])
        kitchen_interval_money_orders_names.to_csv(kitchen_name, sep='\t', index=False)
        kitchen_interval_money_orders_names.to_html(kitchen_name)'''
    get_results_by_kitchen(orders, ['M', 'W', 'D'])
