import pandas as pd
from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())

data = pd.read_csv('data/table_1.csv')



data_condensed = pysqldf("""SELECT case when par_pctile <= 10 then 'Parents Percentile 1-10'
                                        when par_pctile > 10 and par_pctile <= 20 then 'Parents Percentile 11-20'
                                        when par_pctile > 20 and par_pctile <= 30 then 'Parents Percentile 21-30'
                                        when par_pctile > 30 and par_pctile <= 40 then 'Parents Percentile 31-40'
                                        when par_pctile > 40 and par_pctile <= 50 then 'Parents Percentile 41-50'
                                        when par_pctile > 50 and par_pctile <= 60 then 'Parents Percentile 51-60'
                                        when par_pctile > 60 and par_pctile <= 70 then 'Parents Percentile 61-70'
                                        when par_pctile > 70 and par_pctile <= 80 then 'Parents Percentile 71-80'
                                        when par_pctile > 80 and par_pctile <= 90 then 'Parents Percentile 81-90'
                                        when par_pctile > 90 then 'Parents Percentile 91-100' end as par_pctile,
                                    avg(kid_wage_rank_white_male) as kid_wage_rank_white_male,
                                    avg(kid_wage_rank_black_male) as kid_wage_rank_black_male
                            FROM data
                            group by 1;""")

data_condensed.to_csv('data/percentile_race.csv', index=False)

ten_percent = pysqldf("""SELECT *
                            FROM data
                            where par_pctile = 10;""")

ten_percent.to_csv('data/ten_percentile.csv')


ninety_percent = pysqldf("""SELECT *
                            FROM data
                            where par_pctile = 90;""")

ninety_percent.to_csv('data/ninety_percent.csv')