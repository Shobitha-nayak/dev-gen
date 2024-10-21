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



import pdfkit
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# Generate a plot for the report
data = {
    'code_churn': [100, 50, 200, 30],
    'test_coverage': [80, 90, 70, 60]
}

# Create a scatter plot
plt.scatter(data['code_churn'], data['test_coverage'])
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




