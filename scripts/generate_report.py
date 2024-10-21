import pdfkit
import matplotlib.pyplot as plt

# Generate a simple HTML report
html = '''
<h1>DevOps Maturity Report</h1>
<p>Build Success Rate: 90%</p>
<p>Code Churn vs Test Coverage:</p>
<img src="plot.png">
'''

# Generate a plot for report
data = {
    'code_churn': [100, 50, 200, 30],
    'test_coverage': [80, 90, 70, 60]
}
plt.scatter(data['code_churn'], data['test_coverage'])
plt.title("Code Churn vs Test Coverage")
plt.xlabel("Code Churn")
plt.ylabel("Test Coverage")
plt.savefig('plot.png')

# Convert HTML to PDF
pdfkit.from_string(html, 'devops_maturity_report.pdf')

