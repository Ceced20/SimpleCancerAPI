from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

#Sample data not acurate
cancer_stats = {
    'Total_infected': 1000,
    'Active_cases': 500,
    'Recovered': 400,
    'Deaths': 200,
    'Critical': 50,
    'Mortality_rate': 20,
    'deceased': 100,
    'Population': 1000000
}

def update_stats():
    cancer_stats['Total_infected'] +=10
    cancer_stats['Active_cases'] +=10
    cancer_stats['Recovered'] +=10
    cancer_stats['Deaths'] +=10
    cancer_stats['Critical'] +=10
    cancer_stats['Mortality_rate'] +=10
    cancer_stats['deceased'] +=10
    cancer_stats['Population'] +=10
    
def get_cancer_stats():
    return jsonify(cancer_stats)

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_stats, 'interval', minutes=1)
    scheduler.start()
    print('Scheduler started')
    scheduler.print_jobs()
    app.run(debug=True)
