import math
import ru_local as ru

print(ru.v_fuel_galons1)
v_fuel_galons = float(input())
v_fuel_litrs = v_fuel_galons * 3.785
amount_barrels = math.ceil(v_fuel_galons / 19.5)
co2 = v_fuel_galons * 20
equiv_ethanol = v_fuel_galons * 115000
coast_dollars = v_fuel_galons * 3
amount_barrels_prd_RF = 3_699_000
v_fuel_litrs_prd_RF = 3_699_000 * 19.5 * 3.785 / 143_400_000
v_fuel_litras_Nsk_day = v_fuel_litrs_prd_RF * 1_621_500
v_fuel_litras_cntr_year = amount_barrels_prd_RF * 19.5 * 3.785 * 365

print(ru.v_fuel_litrs, v_fuel_litrs)
print(ru.amount_barrels, amount_barrels)
print(ru.co2, co2)
print(ru.equiv_ethanol, equiv_ethanol)
print(ru.coast_dollars, coast_dollars)
print(ru.v_fuel_litras_Nsk_day, v_fuel_litras_Nsk_day)
print(ru.v_fuel_litras_cntr_year, v_fuel_litras_cntr_year)