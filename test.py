
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

WIDTH = 210
HEIGHT = 297
COLS = 2
ROWS = 4
now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")


fig, axs = plt.subplots(ROWS, COLS, figsize=(8,10), squeeze=False)
fig.subplots_adjust(top=0.8)
for ax in axs.flatten():
    ax.set_title("Placeholder", size="medium", weight="bold")
fig.suptitle("Training Data Set", size= "x-large", weight= "bold", y=0.98)
fig.supxlabel("Day", size= "x-large", weight= "bold")
fig.supylabel("VCC", size= "x-large", weight= "bold")
fig.tight_layout()
plt.savefig("test_plot.png", dpi=200)
plt.close()

# Sample Data
data = {
    "Label": ["IGG", "VCC", "Lactate", "Osmo","Feed","Temperature", "pH_setpoint", "DO"],
    "min_": [13, 12.34, 56.78, 90.12,13, 12.34, 56.78, 90.12],
    "max_": [28, 34.56, 78.90, 12.34,28, 34.56, 78.90, 12.34],
    "scale_": [36, 56.78, 90.12, 34.56,36, 56.78, 90.12, 34.56],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting the table and removing all axes
fig_table, ax = plt.subplots(figsize=(6, 2)) # set the size that you'd like (width, height)
ax.axis('off')

tbl = ax.table(cellText=df.values,
               colLabels=df.columns,
               cellLoc='center',
               loc='center'
               )

# Create the table and scale it to fit the fig
for (i, j), cell in tbl.get_celld().items():
    if i == 0:  # header cells
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor("#F25D18")

tbl.auto_set_font_size(False)
tbl.set_fontsize(20)
tbl.scale(2, 4)  # may need to adjust this for your data
plt.savefig("table_image.png", dpi=200, bbox_inches='tight')

d = {}
with open("test.txt",encoding="utf-8") as f:
    for line in f:
        data = line.split(sep=":")
        d[data[0]] = data[1]

pdf = FPDF(format="A4") # A4 (210 by 297 mm)
pdf.add_page()
pdf.set_font("helvetica", "B",8)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)

# Set the title of the document
pdf.set_font('helvetica', 'B', 24)
pdf.set_text_color(r=242, g=93, b=24)
pdf.ln(15)
pdf.write(5, "BDSD State Space Model Report")

# Specify the reference number of document
pdf.set_font('helvetica', 'B', 18)
pdf.set_text_color(r=242, g=93, b=24)
pdf.ln(15)
pdf.write(5, f"IDBS Reference: {d['IDBS']}")

# Write other data to the front cover
pdf.set_font('helvetica', '', 16)
pdf.set_text_color(r=242, g=93, b=24)
pdf.set_text_color(r=0, g=0, b=0)
pdf.ln(13)
pdf.write(7, text=f"Report Generated for {d['Asset']}")
pdf.ln(2)
pdf.write(7, text=f"Dataset for Model Training: {d['Dataset']}")
pdf.ln(2)
pdf.write(7, text=f"States in Model: {d['States']}")
pdf.ln(2)
pdf.write(7, text=f"Inputs in Model: {d['Inputs']}")

pdf.set_font('helvetica', 'B', 18)
pdf.set_text_color(r=242, g=93, b=24)
pdf.ln(10)
pdf.write(7, text=f"Table of Scaler Values from {d['scaler_type']}")

pdf.image("table_image.png", w=160,h=100,x=25,y=125)

pdf.set_font('helvetica', 'I', 16)
pdf.set_text_color(r=0, g=0, b=0)
pdf.ln(127)
pdf.write(7, text=f"Report Author: {d['Author']}")
pdf.ln(2)
pdf.write(7, text=f"GitHub Link: {d['Github']}")
pdf.ln(2)
pdf.write(7, text=f"This report was generated on {now}")

state = "VCC"
pdf.add_page()
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)
# Set the title of the document
pdf.set_font('helvetica', 'B', 24)
pdf.set_text_color(r=242, g=93, b=24)
pdf.ln(5)
pdf.write(5, f"State: {state}")
pdf.image("test_plot.png", w=190,h=250,x=10,y=20)

pdf.add_page()
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)
pdf.image("test_plot.png", w=190,h=250,x=10,y=20)

pdf.add_page()
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)
pdf.image("test_plot.png", w=190,h=250,x=10,y=20)

pdf.add_page()
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)
pdf.image("test_plot.png", w=190,h=250,x=10,y=20)

pdf.add_page()
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)
pdf.image("test_plot.png", w=190,h=250,x=10,y=20)

pdf.add_page()
pdf.image("GSK_logo_2022.png", w=30,h=10,x=170,y=10)
pdf.image("GSK_logo_2022.png", w=30,h=10,x=10,y=277)
# Set the title of the document
pdf.set_font('helvetica', 'B', 24)
pdf.set_text_color(r=242, g=93, b=24)
pdf.ln(5)
pdf.write(5, f"State: IGG")
pdf.image("test_plot.png", w=190,h=250,x=10,y=20)

pdf.output("text.pdf")
