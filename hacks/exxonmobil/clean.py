import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

class InventoryDataCleaner:
    def __init__(self):
        self.inventory_df = None
        self.inbound_df = None
        self.outbound_df = None
        self.material_df = None
        self.operation_cost_df = None
        self.forecast_df = None
        self.cleaned_data = {}
        
    def load_data(self, file_paths=None):
        """Load all CSV files. If file_paths not provided, assumes default naming."""
        if file_paths is None:
            file_paths = {
                'inventory': 'Inventory.csv',
                'inbound': 'Inbound.csv',
                'outbound': 'Outbound.csv',
                'material': 'MaterialMaster.csv',
                'operation_cost': 'OperationCost.csv',
                'forecast': 'Forecast.xlsx'
            }
        
        try:
            print("Loading data files...")
            self.inventory_df = pd.read_csv(file_paths['inventory'])
            self.inbound_df = pd.read_csv(file_paths['inbound'])
            self.outbound_df = pd.read_csv(file_paths['outbound'])
            self.material_df = pd.read_csv(file_paths['material'])
            self.operation_cost_df = pd.read_csv(file_paths['operation_cost'])
            
            # Handle Excel file
            if file_paths['forecast'].endswith('.xlsx'):
                self.forecast_df = pd.read_excel(file_paths['forecast'])
            else:
                self.forecast_df = pd.read_csv(file_paths['forecast'])
                
            print("[SUCCESS] All files loaded successfully!")
            self._print_data_overview()
            
        except FileNotFoundError as e:
            print(f"[ERROR] File not found: {e}")
            print("Please ensure all required files are in the correct directory.")
            
    def _print_data_overview(self):
        """Print overview of loaded datasets"""
        datasets = {
            'Inventory': self.inventory_df,
            'Inbound': self.inbound_df,
            'Outbound': self.outbound_df,
            'Material': self.material_df,
            'Operation Cost': self.operation_cost_df,
            'Forecast': self.forecast_df
        }
        
        print("\n[INFO] DATA OVERVIEW:")
        print("-" * 50)
        for name, df in datasets.items():
            if df is not None:
                print(f"{name:15}: {df.shape[0]:6,} rows x {df.shape[1]:2} columns")
            else:
                print(f"{name:15}: Not loaded")
    
    def clean_inventory_data(self):
        """Clean inventory dataset"""
        print("\n[CLEANING] Cleaning Inventory Data...")
        df = self.inventory_df.copy()
        
        # Convert date column
        df['BALANCE_AS_OF_DATE'] = pd.to_datetime(df['BALANCE_AS_OF_DATE'])
        
        # Convert stock to MT (from KG if needed)
        df['STOCK_MT'] = df['UNRESRICTED_STOCK'].copy()
        if df['STOCK_UNIT'].iloc[0] == 'KG':
            df['STOCK_MT'] = df['UNRESRICTED_STOCK'] / 1000  # Convert KG to MT
        
        # Clean up text columns
        df['PLANT_NAME'] = df['PLANT_NAME'].str.strip().str.upper()
        df['MATERIAL_NAME'] = df['MATERIAL_NAME'].str.strip()
        
        # Remove negative or zero stocks (data quality issue)
        df = df[df['STOCK_MT'] > 0]
        
        # Add month-year column for aggregation
        df['YEAR_MONTH'] = df['BALANCE_AS_OF_DATE'].dt.to_period('M')
        
        self.cleaned_data['inventory'] = df
        print(f"[SUCCESS] Cleaned inventory data: {len(df):,} records")
        return df
    
    def clean_inbound_data(self):
        """Clean inbound dataset"""
        print("\n[CLEANING] Cleaning Inbound Data...")
        df = self.inbound_df.copy()
        
        # Convert date
        df['INBOUND_DATE'] = pd.to_datetime(df['INBOUND_DATE'])
        
        # Clean text columns
        df['PLANT_NAME'] = df['PLANT_NAME'].str.strip().str.upper()
        df['MATERIAL_NAME'] = df['MATERIAL_NAME'].str.strip()
        
        # Remove negative quantities
        df = df[df['NET_QUANTITY_MT'] > 0]
        
        # Add month-year for aggregation
        df['YEAR_MONTH'] = df['INBOUND_DATE'].dt.to_period('M')
        
        self.cleaned_data['inbound'] = df
        print(f"[SUCCESS] Cleaned inbound data: {len(df):,} records")
        return df
    
    def clean_outbound_data(self):
        """Clean outbound dataset"""
        print("\n[CLEANING] Cleaning Outbound Data...")
        df = self.outbound_df.copy()
        
        # Convert date
        df['OUTBOUND_DATE'] = pd.to_datetime(df['OUTBOUND_DATE'])
        
        # Clean text columns
        df['PLANT_NAME'] = df['PLANT_NAME'].str.strip().str.upper()
        df['MATERIAL_NAME'] = df['MATERIAL_NAME'].str.strip()
        df['MODE_OF_TRANSPORT'] = df['MODE_OF_TRANSPORT'].str.strip()
        
        # Remove negative quantities
        df = df[df['NET_QUANTITY_MT'] > 0]
        
        # Add month-year for aggregation
        df['YEAR_MONTH'] = df['OUTBOUND_DATE'].dt.to_period('M')
        
        self.cleaned_data['outbound'] = df
        print(f"[SUCCESS] Cleaned outbound data: {len(df):,} records")
        return df
    
    def clean_material_data(self):
        """Clean material master data"""
        print("\n[CLEANING] Cleaning Material Master Data...")
        df = self.material_df.copy()
        
        # Clean text columns
        df['MATERIAL_NAME'] = df['MATERIAL_NAME'].str.strip()
        df['POLYMER_TYPE'] = df['POLYMER_TYPE'].str.strip()
        
        # Handle missing values
        df['SHELF_LIFE_IN_MONTH'] = df['SHELF_LIFE_IN_MONTH'].fillna(12)  # Default 12 months
        df['DOWNGRADE_VALUE_LOST_PERCENT'] = df['DOWNGRADE_VALUE_LOST_PERCENT'].fillna(20)  # Default 20%
        
        self.cleaned_data['material'] = df
        print(f"[SUCCESS] Cleaned material data: {len(df):,} records")
        return df
    
    def create_monthly_aggregated_data(self):
        """Create monthly aggregated dataset for analysis"""
        print("\n[PROCESSING] Creating Monthly Aggregated Dataset...")
        
        # Monthly inventory (end of month snapshot)
        monthly_inventory = (self.cleaned_data['inventory']
                           .groupby(['PLANT_NAME', 'MATERIAL_NAME', 'YEAR_MONTH'])
                           .agg({
                               'STOCK_MT': 'sum',
                               'STOCK_SELL_VALUE': 'sum'
                           }).reset_index())
        
        # Monthly inbound
        monthly_inbound = (self.cleaned_data['inbound']
                         .groupby(['PLANT_NAME', 'MATERIAL_NAME', 'YEAR_MONTH'])
                         .agg({
                             'NET_QUANTITY_MT': 'sum'
                         }).reset_index()
                         .rename(columns={'NET_QUANTITY_MT': 'INBOUND_MT'}))
        
        # Monthly outbound
        monthly_outbound = (self.cleaned_data['outbound']
                          .groupby(['PLANT_NAME', 'MATERIAL_NAME', 'YEAR_MONTH'])
                          .agg({
                              'NET_QUANTITY_MT': 'sum'
                          }).reset_index()
                          .rename(columns={'NET_QUANTITY_MT': 'OUTBOUND_MT'}))
        
        # Combine all monthly data
        monthly_combined = monthly_inventory.merge(
            monthly_inbound, 
            on=['PLANT_NAME', 'MATERIAL_NAME', 'YEAR_MONTH'], 
            how='outer'
        ).merge(
            monthly_outbound, 
            on=['PLANT_NAME', 'MATERIAL_NAME', 'YEAR_MONTH'], 
            how='outer'
        )
        
        # Fill missing values with 0
        monthly_combined = monthly_combined.fillna(0)
        
        # Add material master information
        monthly_combined = monthly_combined.merge(
            self.cleaned_data['material'][['MATERIAL_NAME', 'POLYMER_TYPE', 'SHELF_LIFE_IN_MONTH']],
            on='MATERIAL_NAME',
            how='left'
        )
        
        self.cleaned_data['monthly_combined'] = monthly_combined
        print(f"[SUCCESS] Created monthly dataset: {len(monthly_combined):,} records")
        return monthly_combined
    
    def calculate_inventory_flow(self):
        """Calculate inventory flow and identify potential overflow periods"""
        print("\n[PROCESSING] Calculating Inventory Flow...")
        
        df = self.cleaned_data['monthly_combined'].copy()
        df = df.sort_values(['PLANT_NAME', 'MATERIAL_NAME', 'YEAR_MONTH'])
        
        # Calculate net change
        df['NET_CHANGE_MT'] = df['INBOUND_MT'] - df['OUTBOUND_MT']
        
        # Calculate rolling inventory (simplified)
        df['CALCULATED_INVENTORY_MT'] = df.groupby(['PLANT_NAME', 'MATERIAL_NAME'])['NET_CHANGE_MT'].cumsum()
        
        # Convert period to datetime for easier plotting
        df['DATE'] = df['YEAR_MONTH'].dt.to_timestamp()
        
        self.cleaned_data['inventory_flow'] = df
        print("[SUCCESS] Calculated inventory flow")
        return df
    
    def identify_high_risk_periods(self, capacity_threshold_mt=1000):
        """Identify periods with high overflow risk"""
        print(f"\n[ANALYSIS] Identifying High Risk Periods (Threshold: {capacity_threshold_mt} MT)...")
        
        # Aggregate by plant and month
        plant_monthly = (self.cleaned_data['inventory_flow']
                        .groupby(['PLANT_NAME', 'YEAR_MONTH'])
                        .agg({
                            'STOCK_MT': 'sum',
                            'INBOUND_MT': 'sum',
                            'OUTBOUND_MT': 'sum',
                            'NET_CHANGE_MT': 'sum'
                        }).reset_index())
        
        # Flag high risk periods
        plant_monthly['RISK_LEVEL'] = pd.cut(
            plant_monthly['STOCK_MT'], 
            bins=[0, capacity_threshold_mt*0.7, capacity_threshold_mt*0.9, capacity_threshold_mt, float('inf')],
            labels=['Safe', 'Medium', 'High', 'Overflow'],
            include_lowest=True
        )
        
        plant_monthly['CAPACITY_UTILIZATION'] = plant_monthly['STOCK_MT'] / capacity_threshold_mt * 100
        
        self.cleaned_data['risk_analysis'] = plant_monthly
        
        # Print risk summary
        risk_summary = plant_monthly['RISK_LEVEL'].value_counts()
        print("[INFO] Risk Level Distribution:")
        for level, count in risk_summary.items():
            print(f"   {level}: {count} periods")
        
        return plant_monthly
    
    def generate_summary_report(self):
        """Generate a summary report of the cleaned data"""
        print("\n[REPORT] SUMMARY REPORT")
        print("=" * 60)
        
        # Date range
        inbound_date_range = f"{self.cleaned_data['inbound']['INBOUND_DATE'].min().strftime('%Y-%m')} to {self.cleaned_data['inbound']['INBOUND_DATE'].max().strftime('%Y-%m')}"
        outbound_date_range = f"{self.cleaned_data['outbound']['OUTBOUND_DATE'].min().strftime('%Y-%m')} to {self.cleaned_data['outbound']['OUTBOUND_DATE'].max().strftime('%Y-%m')}"
        
        print(f"[INFO] Data Period:")
        print(f"   Inbound: {inbound_date_range}")
        print(f"   Outbound: {outbound_date_range}")
        
        # Plants and materials
        plants = self.cleaned_data['inventory']['PLANT_NAME'].nunique()
        materials = self.cleaned_data['inventory']['MATERIAL_NAME'].nunique()
        
        print(f"\n[INFO] Scope:")
        print(f"   Plants: {plants}")
        print(f"   Materials: {materials}")
        
        # Volume summary
        total_inbound = self.cleaned_data['inbound']['NET_QUANTITY_MT'].sum()
        total_outbound = self.cleaned_data['outbound']['NET_QUANTITY_MT'].sum()
        current_inventory = self.cleaned_data['inventory']['STOCK_MT'].sum()
        
        print(f"\n[INFO] Volume Summary (MT):")
        print(f"   Total Inbound: {total_inbound:,.0f}")
        print(f"   Total Outbound: {total_outbound:,.0f}")
        print(f"   Current Inventory: {current_inventory:,.0f}")
        print(f"   Net Change: {total_inbound - total_outbound:+,.0f}")
        
        # Top materials by volume
        top_materials = (self.cleaned_data['inventory']
                        .groupby('MATERIAL_NAME')['STOCK_MT']
                        .sum()
                        .sort_values(ascending=False)
                        .head(5))
        
        print(f"\n[INFO] Top 5 Materials by Inventory:")
        for material, volume in top_materials.items():
            print(f"   {material}: {volume:,.0f} MT")
    
    def visualize_data(self, save_plots=True):
        """Create visualizations for the cleaned data"""
        print("\n[VISUALIZING] Creating Visualizations...")
        
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 15))
        
        # 1. Monthly Inventory Trend by Plant
        plt.subplot(2, 3, 1)
        plant_trend = (self.cleaned_data['inventory_flow']
                      .groupby(['PLANT_NAME', 'YEAR_MONTH'])['STOCK_MT']
                      .sum().unstack(level=0, fill_value=0))
        
        for plant in plant_trend.columns:
            plt.plot(plant_trend.index.to_timestamp(), plant_trend[plant], 
                    marker='o', label=plant, linewidth=2)
        
        plt.title('Monthly Inventory Trend by Plant', fontsize=14, fontweight='bold')
        plt.xlabel('Month')
        plt.ylabel('Inventory (MT)')
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        # 2. Inbound vs Outbound Comparison
        plt.subplot(2, 3, 2)
        monthly_flow = (self.cleaned_data['inventory_flow']
                       .groupby('YEAR_MONTH')
                       .agg({'INBOUND_MT': 'sum', 'OUTBOUND_MT': 'sum'}))
        
        x = range(len(monthly_flow))
        width = 0.35
        plt.bar([i - width/2 for i in x], monthly_flow['INBOUND_MT'], 
               width, label='Inbound', color='green', alpha=0.7)
        plt.bar([i + width/2 for i in x], monthly_flow['OUTBOUND_MT'], 
               width, label='Outbound', color='red', alpha=0.7)
        
        plt.title('Monthly Inbound vs Outbound', fontsize=14, fontweight='bold')
        plt.xlabel('Month')
        plt.ylabel('Quantity (MT)')
        plt.legend()
        plt.xticks(x, [str(period) for period in monthly_flow.index], rotation=45)
        plt.grid(True, alpha=0.3)
        
        # 3. Material Distribution
        plt.subplot(2, 3, 3)
        material_dist = (self.cleaned_data['inventory']
                        .groupby('MATERIAL_NAME')['STOCK_MT']
                        .sum().sort_values(ascending=False).head(10))
        
        plt.barh(range(len(material_dist)), material_dist.values, color='skyblue')
        plt.yticks(range(len(material_dist)), material_dist.index)
        plt.title('Top 10 Materials by Inventory', fontsize=14, fontweight='bold')
        plt.xlabel('Inventory (MT)')
        plt.grid(True, alpha=0.3)
        
        # 4. Risk Level Distribution
        if 'risk_analysis' in self.cleaned_data:
            plt.subplot(2, 3, 4)
            risk_dist = self.cleaned_data['risk_analysis']['RISK_LEVEL'].value_counts()
            colors = {'Safe': 'green', 'Medium': 'orange', 'High': 'red', 'Overflow': 'darkred'}
            risk_colors = [colors.get(level, 'gray') for level in risk_dist.index]
            
            plt.pie(risk_dist.values, labels=risk_dist.index, autopct='%1.1f%%', 
                   colors=risk_colors, startangle=90)
            plt.title('Risk Level Distribution', fontsize=14, fontweight='bold')
        
        # 5. Capacity Utilization Timeline
        if 'risk_analysis' in self.cleaned_data:
            plt.subplot(2, 3, 5)
            capacity_timeline = self.cleaned_data['risk_analysis'].groupby('YEAR_MONTH')['CAPACITY_UTILIZATION'].mean()
            
            plt.plot(capacity_timeline.index.to_timestamp(), capacity_timeline.values, 
                    marker='o', linewidth=3, color='purple')
            plt.axhline(y=90, color='red', linestyle='--', label='High Risk (90%)')
            plt.axhline(y=70, color='orange', linestyle='--', label='Medium Risk (70%)')
            
            plt.title('Average Capacity Utilization Over Time', fontsize=14, fontweight='bold')
            plt.xlabel('Month')
            plt.ylabel('Capacity Utilization (%)')
            plt.legend()
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
        
        # 6. Polymer Type Distribution
        plt.subplot(2, 3, 6)
        if 'material' in self.cleaned_data:
            # Merge inventory with material data to get polymer types
            inventory_with_polymer = self.cleaned_data['inventory'].merge(
                self.cleaned_data['material'][['MATERIAL_NAME', 'POLYMER_TYPE']], 
                on='MATERIAL_NAME', how='left'
            )
            
            polymer_dist = (inventory_with_polymer
                           .groupby('POLYMER_TYPE')['STOCK_MT']
                           .sum().sort_values(ascending=False))
            
            plt.bar(polymer_dist.index, polymer_dist.values, color='lightcoral')
            plt.title('Inventory by Polymer Type', fontsize=14, fontweight='bold')
            plt.xlabel('Polymer Type')
            plt.ylabel('Inventory (MT)')
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_plots:
            plt.savefig('inventory_analysis_dashboard.png', dpi=300, bbox_inches='tight')
            print("[SUCCESS] Visualizations saved as 'inventory_analysis_dashboard.png'")
        
        plt.show()
    
    def export_cleaned_data(self, output_dir='cleaned_data/'):
        """Export cleaned datasets"""
        import os
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(f"\n[EXPORT] Exporting Cleaned Data to '{output_dir}'...")
        
        for name, df in self.cleaned_data.items():
            if df is not None:
                filename = f"{output_dir}{name}_cleaned.csv"
                df.to_csv(filename, index=False)
                print(f"   [SUCCESS] {name}_cleaned.csv")
        
        print("[SUCCESS] All cleaned datasets exported successfully!")
    
    def run_complete_analysis(self, capacity_threshold_mt=1000):
        """Run the complete data cleaning and analysis pipeline"""
        print("[START] STARTING COMPLETE INVENTORY ANALYSIS")
        print("=" * 60)
        
        # Clean all datasets
        self.clean_inventory_data()
        self.clean_inbound_data()
        self.clean_outbound_data()
        self.clean_material_data()
        
        # Create aggregated data
        self.create_monthly_aggregated_data()
        self.calculate_inventory_flow()
        self.identify_high_risk_periods(capacity_threshold_mt)
        
        # Generate reports and visualizations
        self.generate_summary_report()
        self.visualize_data()
        
        # Export cleaned data
        self.export_cleaned_data()
        
        print("\n[COMPLETE] ANALYSIS COMPLETE!")
        print("=" * 60)
        
        return self.cleaned_data


# Example usage
if __name__ == "__main__":
    # Initialize the cleaner
    cleaner = InventoryDataCleaner()
    
    # Load your data files (update paths as needed)
    file_paths = {
        'inventory': 'Inventory.csv',
        'inbound': 'Inbound.csv', 
        'outbound': 'Outbound.csv',
        'material': 'MaterialMaster.csv',
        'operation_cost': 'OperationCost.csv',
        'forecast': 'Forecast.xlsx'
    }
    
    # Load data
    cleaner.load_data(file_paths)
    
    # Run complete analysis
    # Set capacity_threshold_mt to your actual warehouse capacity
    cleaned_data = cleaner.run_complete_analysis(capacity_threshold_mt=1000)
    
    # Access specific cleaned datasets
    monthly_data = cleaned_data['monthly_combined']
    risk_analysis = cleaned_data['risk_analysis']
    
    print("\n[NEXT STEPS] NEXT STEPS FOR HACKATHON:")
    print("1. Review the generated visualizations")
    print("2. Use 'monthly_combined' dataset for building ML models")
    print("3. Use 'risk_analysis' for overflow prediction")
    print("4. Adjust capacity_threshold_mt to your actual warehouse capacity")
    print("5. Build forecasting model using cleaned data!")