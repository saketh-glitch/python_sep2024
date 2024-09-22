from database import Database
import pandas as pd 
class Reports:
    def __init__(self):
        self.db =Database() 

    def generate_inventory_report(self):
        data = self.db.fetch_all_materials()
        df = pd.DataFrame(data, columns=['ID', 'Name', 'Quantity', 'Reorder_level','Price','Historical_sales']) 
        df['Turnover'] = df['Quantity'] * 10  # Example turnover formula
        return df

    def forecast_demand(self):
        '''df = self.generate_inventory_report()
        # Simple forecasting logic
        df['Forecast'] = df['Turnover'].rolling(window=3).mean()
        return df[['Name', 'Forecast']]'''
        print("Generating forecast report...")
        data = pd.DataFrame(self.db.fetch_all_materials(), columns=['id', 'name', 'stock','Threshold', 'cost_of_goods_sold', 'historical_sales'])
        data["forecasted_sales"] = data["historical_sales"] * 1.1  # 10% growth
        print("\n--- Forecast Report ---")
        print(data[["id", "name", "forecasted_sales"]])

    def generate_turnover_report(self):  
        all_materials = self.db.fetch_all_materials()
        for material in all_materials:
            Item_id, Name, Stock, Reorder_threshold, Price_of_material, Historical_sales = material
            turnover_rate = Historical_sales / Price_of_material
            print(f" \n Material: {Name} (ID: {Item_id}) - Turnover Rate: {turnover_rate:.2f}") 


