
import pandas as pd
import plotly.express as px

df = pd.read_excel("clean/clean_uk_emp_v2.xlsx")


class EmploymentAnalysis:
    def __init__(self, data_frame):
        
        self.df = data_frame
        
        self.df['Year'] = self.df['Year'].dt.year
        self.df.set_index('Year',inplace=True)
        
        # Sector data
        self.sector_data = self.df[['Employment in agriculture (% of total employment) (modeled ILO estimate)',
                                'Employment in industry (% of total employment) (modeled ILO estimate)',
                                'Employment in services (% of total employment) (modeled ILO estimate)']]
        self.sector_data.columns = ['Agriculture', 'Industry', 'Services']
    
        # unemployment data
        self.unemployment_data = self.df[['Unemployment, male (% of male labor force) (modeled ILO estimate)',
                                       'Unemployment, female (% of female labor force) (modeled ILO estimate)']]
        self.unemployment_data.columns = ['Male', 'Female'] 
    
        # part time employment data
        self.part_time_data = self.df[['Part time employment, male (% of total male employment)',
                                   'Part time employment, female (% of total female employment)']]
        self.part_time_data.columns = ['Male', 'Female']
    
    
    def employment_by_sector(self, slct_sect):
   
        data = self.sector_data.copy()
        data = pd.DataFrame(data[slct_sect])
        
        fig = px.line(data, x=data.index, y=data.columns)
        
        fig.update_layout(yaxis_title='Percentage of Total Employment',
                        xaxis_title='Year')
        fig.update_xaxes(tickmode='linear')
        
        return fig

    def gender_unemployment_gap(self, slct_sect):
        
        data = self.unemployment_data.copy()
        data = pd.DataFrame(data[slct_sect])

        fig = px.line(data, x=data.index, y=data.columns,
                       title='Gender Unemployment Gap')
        fig.update_layout(yaxis_title='Unemployment Rate (%)', xaxis_title='Year')

        return fig

    def part_time_employment(self, slct_sect):

        data = self.part_time_data.copy()
        data = pd.DataFrame(data[slct_sect])

        fig = px.line(data, x=data.index, y=data.columns,
                       title="Part-time Employment Rate by Gender")
        fig.update_layout(xaxis_title='Year', yaxis_title="Part-time Employment %")

        return fig






