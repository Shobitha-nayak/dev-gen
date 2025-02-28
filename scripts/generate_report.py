# # import pdfkit
# # import matplotlib.pyplot as plt

# # # Generate a simple HTML report
# # html = '''
# # <h1>DevOps Maturity Report</h1>
# # <p>Build Success Rate: 90%</p>
# # <p>Code Churn vs Test Coverage:</p>
# # <img src="plot.png">
# # '''

# # # Generate a plot for report
# # data = {
# #     'code_churn': [100, 50, 200, 30],
# #     'test_coverage': [80, 90, 70, 60]
# # }
# # plt.scatter(data['code_churn'], data['test_coverage'])
# # plt.title("Code Churn vs Test Coverage")
# # plt.xlabel("Code Churn")
# # plt.ylabel("Test Coverage")
# # plt.savefig('plot.png')

# # # Convert HTML to PDF
# # pdfkit.from_string(html, 'devops_maturity_report.pdf')


# # import pdfkit
# # import matplotlib.pyplot as plt
# # import os

# # # Generate a plot for the report
# # data = {
# #     'code_churn': [100, 50, 200, 30],
# #     'test_coverage': [80, 90, 70, 60]
# # }
# # plt.scatter(data['code_churn'], data['test_coverage'])
# # plt.title("Code Churn vs Test Coverage")
# # plt.xlabel("Code Churn")
# # plt.ylabel("Test Coverage")
# # # Save the plot as a PNG file
# # plot_path = os.path.join(os.getcwd(), 'plot.png')
# # plt.savefig(plot_path)
# # plt.close()  # Close the plot to free up memory

# # # Generate a simple HTML report
# # html = f'''
# # <h1>DevOps Maturity Report</h1>
# # <p>Build Success Rate: 90%</p>
# # <p>Code Churn vs Test Coverage:</p>
# # <img src="plot.png">  <!-- Ensure this is the correct path -->
# # '''

# # # Convert HTML to PDF
# # output_pdf_path = os.path.join(os.getcwd(), 'devops_maturity_report.pdf')
# # pdfkit.from_string(html, output_pdf_path)

# # print(f"Report generated successfully: {output_pdf_path}")




# import pdfkit
# import matplotlib.pyplot as plt
# import os

# # Generate a plot for the report
# data = {
#     'code_churn': [100, 50, 200, 30],
#     'test_coverage': [80, 90, 70, 60]
# }

# # Create the plot
# plt.scatter(data['code_churn'], data['test_coverage'])
# plt.title("Code Churn vs Test Coverage")
# plt.xlabel("Code Churn")
# plt.ylabel("Test Coverage")

# # Save the plot as a PNG file in the 'scripts' directory
# plot_path = os.path.join('scripts', 'plot.png')
# plt.savefig(plot_path)
# plt.close()  # Close the plot to free up memory

# # Generate a simple HTML report
# html = f'''
# <h1>DevOps Maturity Report</h1>
# <p>Build Success Rate: 90%</p>
# <p>Code Churn vs Test Coverage:</p>
# <img src="file://{os.path.abspath(plot_path)}">  <!-- Use absolute path -->
# '''

# # Convert HTML to PDF
# output_pdf_path = os.path.join('scripts', 'devops_maturity_report.pdf')
# pdfkit.from_string(html, output_pdf_path)

# print(f"Report generated successfully: {output_pdf_path}")








# import pdfkit
# import matplotlib.pyplot as plt

# # Generate a simple HTML report
# html = '''
# <h1>DevOps Maturity Report</h1>
# <p>Build Success Rate: 90%</p>
# <p>Code Churn vs Test Coverage:</p>
# <img src="plot.png">
# '''

# # Generate a plot for report
# data = {
#     'code_churn': [100, 50, 200, 30],
#     'test_coverage': [80, 90, 70, 60]
# }
# plt.scatter(data['code_churn'], data['test_coverage'])
# plt.title("Code Churn vs Test Coverage")
# plt.xlabel("Code Churn")
# plt.ylabel("Test Coverage")
# plt.savefig('plot.png')

# # Convert HTML to PDF
# pdfkit.from_string(html, 'devops_maturity_report.pdf')




# import pdfkit
# import matplotlib.pyplot as plt
# import os

# # Generate a plot for report
# data = {
#     'code_churn': [100, 50, 200, 30],
#     'test_coverage': [80, 90, 70, 60]
# }
# plt.scatter(data['code_churn'], data['test_coverage'])
# plt.title("Code Churn vs Test Coverage")
# plt.xlabel("Code Churn")
# plt.ylabel("Test Coverage")
# plt.savefig('plot.png')
# plt.close()  # Close the plot to free up memory

# # Generate a simple HTML report
# html = f'''
# <h1>DevOps Maturity Report</h1>
# <p>Build Success Rate: 90%</p>
# <p>Code Churn vs Test Coverage:</p>
# <img src="{os.path.abspath('plot.png')}">
# '''

# # Convert HTML to PDF
# pdfkit.from_string(html, 'devops_maturity_report.pdf')




# import pdfkit
# import matplotlib.pyplot as plt
# import os

# # Generate a plot for the report
# data = {
#     'code_churn': [100, 50, 200, 30],
#     'test_coverage': [80, 90, 70, 60]
# }

# # Create a scatter plot
# plt.scatter(data['code_churn'], data['test_coverage'])
# plt.title("Code Churn vs Test Coverage")
# plt.xlabel("Code Churn")
# plt.ylabel("Test Coverage")
# plt.savefig('plot.png')  # Save the plot as a PNG file
# plt.close()  # Close the plot to avoid display

# # Generate a simple HTML report
# html = f'''
# <h1>DevOps Maturity Report</h1>
# <p>Build Success Rate: 90%</p>
# <p>Code Churn vs Test Coverage:</p>
# <img src="{os.path.abspath('plot.png')}" alt="Code Churn vs Test Coverage">
# '''

# # Print HTML content for debugging
# print("Generated HTML for report:")
# print(html)

# # Convert HTML to PDF
# try:
#     pdfkit.from_string(html, 'devops_maturity_report.pdf')
#     print("PDF generated successfully!")
# except Exception as e:
#     print(f"Error generating PDF: {e}")



# import pdfkit
# import matplotlib.pyplot as plt
# import os

# # Ensure output directory exists
# output_dir = 'outputs'
# os.makedirs(output_dir, exist_ok=True)

# # Generate a plot for the report
# data = {
#     'code_churn': [100, 50, 200, 30],
#     'test_coverage': [80, 90, 70, 60]
# }

# # Create a scatter plot
# plt.scatter(data['code_churn'], data['test_coverage'])
# plt.title("Code Churn vs Test Coverage")
# plt.xlabel("Code Churn")
# plt.ylabel("Test Coverage")
# plt.savefig(os.path.join(output_dir, 'plot.png'))  # Save in outputs directory
# plt.close()  # Close the plot to avoid display

# # Generate a simple HTML report
# html = f'''
# <h1>DevOps Maturity Report</h1>
# <p>Build Success Rate: 90%</p>
# <p>Code Churn vs Test Coverage:</p>
# <p><strong>Test Coverage:</strong> 85%</p>
# <p><strong>Insights:</strong> The team is focusing more on bug fixes in recent sprints.</p>
# <img src="{os.path.abspath(os.path.join(output_dir, 'plot.png'))}" alt="Code Churn vs Test Coverage">
# '''

# # Print HTML content for debugging
# print("Generated HTML for report:")
# print(html)

# # Convert HTML to PDF
# try:
#     pdfkit.from_string(html, os.path.join(output_dir, 'devops_maturity_report.pdf'))  # Save PDF in outputs directory
#     print("PDF generated successfully!")
# except Exception as e:
#     print(f"Error generating PDF: {e}")


# import pdfkit
# import matplotlib.pyplot as plt
# import os
# import json

# # Ensure output directory exists
# output_dir = 'outputs'
# os.makedirs(output_dir, exist_ok=True)

# # Load data
# with open('outputs/commit_data.json', 'r') as f:
#     commit_data = json.load(f)
# with open('outputs/build_success_rate.txt', 'r') as f:
#     build_success_rate = f.read()
# with open('outputs/insights.txt', 'r') as f:
#     insights = f.read()

# # Example data for plotting (use actual data in a real-world case)
# data = {
#     'code_churn': [100, 50, 200, 30],  # Simplified for example
#     'test_coverage': [80, 90, 70, 60]  # Simplified for example
# }

# # Generate a scatter plot
# plt.scatter(data['code_churn'], data['test_coverage'])
# plt.title("Code Churn vs Test Coverage")
# plt.xlabel("Code Churn")
# plt.ylabel("Test Coverage")
# plt.savefig(os.path.join(output_dir, 'plot.png'))  # Save in outputs directory
# plt.close()  # Close plot to avoid display

# # Generate the HTML report
# html = f'''
# <h1>DevOps Maturity Report</h1>
# <p>Build Success Rate: {build_success_rate}%</p>
# <p>Code Churn vs Test Coverage:</p>
# <p><strong>Test Coverage:</strong> {sum(data['test_coverage']) / len(data['test_coverage'])}%</p>
# <p><strong>Insights:</strong> {insights}</p>
# <img src="{os.path.abspath(os.path.join(output_dir, 'plot.png'))}" alt="Code Churn vs Test Coverage">
# '''

# # Print HTML for debugging
# print("Generated HTML report:")
# print(html)

# # Convert HTML to PDF
# try:
#     pdfkit.from_string(html, os.path.join(output_dir, 'devops_maturity_report.pdf'))
#     print("PDF generated successfully!")
# except Exception as e:
#     print(f"Error generating PDF: {e}")







import pdfkit
import matplotlib.pyplot as plt
import os
import json

# Ensure output directory exists
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Load the commit analysis data
with open('scripts/data/commit_analysis.json', 'r') as f:
    analyses = json.load(f)

# Calculate insights
total_commits = len(analyses)
insight_summary = "\n".join(f"Commit: {a['commit_message']}\nAnalysis: {a['analysis']}" for a in analyses)

# Dummy data for plotting (in a real scenario, replace this with actual data)
code_churn = [100, 50, 200, 30]  # This should be calculated from commit data
test_coverage = [80, 90, 70, 60]  # This could be fetched from a testing tool

# Create a scatter plot
plt.scatter(code_churn, test_coverage)
plt.title("Code Churn vs Test Coverage")
plt.xlabel("Code Churn")
plt.ylabel("Test Coverage")
plt.savefig(os.path.join(output_dir, 'plot.png'))  # Save in outputs directory
plt.close()  # Close the plot to avoid display

# Generate a simple HTML report
html = f'''
<h1>DevOps Maturity Report</h1>
<p>Build Success Rate: 90%</p>
<p>Code Churn vs Test Coverage:</p>
<p><strong>Test Coverage:</strong> 85%</p>
<p><strong>Insights from Commit Analyses:The majority of commits are feature additions.</strong></p>
<pre>{insight_summary}</pre>
<img src="{os.path.abspath(os.path.join(output_dir, 'plot.png'))}" alt="Code Churn vs Test Coverage">
'''

# Print HTML content for debugging
print("Generated HTML for report:")
print(html)

# Convert HTML to PDF
try:
    pdfkit.from_string(html, os.path.join(output_dir, 'devops_maturity_report.pdf'))  # Save PDF in outputs directory
    print("PDF generated successfully!")
except Exception as e:
    print(f"Error generating PDF: {e}")






