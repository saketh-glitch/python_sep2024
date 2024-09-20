from database import Database

class Reports:
    def __init__(self):
        self.db = Database()

    def generate_turnover_report(self):
        """Generate inventory turnover report based on historical data"""
        all_materials = self.db.fetch_all_materials()
        for material in all_materials:
            item_id, name, stock, reorder_threshold, cost_of_goods_sold, historical_sales = material
            turnover_rate = historical_sales / cost_of_goods_sold
            print(f"Material: {name} (ID: {item_id}) - Turnover Rate: {turnover_rate:.2f}")