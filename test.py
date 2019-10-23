from process_files import BaseFile, BasicCupcakes

basic_cupcake = BasicCupcakes(file_path='csv_src/Basic.txt', price=5)
print(basic_cupcake.year_total_amount)
print(basic_cupcake.month_total_amount)
print(basic_cupcake.week_total_amount)