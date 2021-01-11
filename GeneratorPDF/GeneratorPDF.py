import os 
import sys

from fpdf import FPDF


def mark_High_pressure_pump(pdf): # ТНВД
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)
    # Marked area High pressure on image 
    x1_rect = 112
    y1_rect = 80
    x2_rect = 118
    y2_rect = 90

    pdf.set_fill_color(255, 0, 0)
    pdf.ellipse((x1_rect + x2_rect) / 2 - 1, (y1_rect + y2_rect) / 2 - 1, 2, 2, 'F')
    # pdf.line(x1_rect, y1_rect, x1_rect, y2_rect)
    # pdf.line(x1_rect, y1_rect, x2_rect, y1_rect)
    # pdf.line(x2_rect, y1_rect, x2_rect, y2_rect)
    # pdf.line(x1_rect, y2_rect, x2_rect, y2_rect)

    # Set name  
    pdf.line((x1_rect + x2_rect) / 2, (y1_rect + y2_rect) / 2, x2_rect + 2, y2_rect - 10)
    pdf.line(x2_rect + 2, y2_rect - 10, x2_rect + 30, y2_rect - 10)

    #pdf.cell(x2_rect + 640, y2_rect - 134, "Fuel Filter", ln=1)

def mark_Fuel_filter(pdf): # Топливный фильтр
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)
    
    # Marked area High pressure on image 
    x1_rect = 112
    y1_rect = 80
    x2_rect = 118
    y2_rect = 90
    pdf.set_fill_color(255, 0, 0)
    pdf.ellipse((x1_rect + x2_rect) / 2 - 1, (y1_rect + y2_rect) / 2 - 5, 2, 2, 'F')

    # Set name  
    pdf.line((x1_rect + x2_rect) / 2, (y1_rect + y2_rect) / 2 - 4, x2_rect + 2, y2_rect - 16)
    pdf.line(x2_rect + 2, y2_rect - 16, x2_rect + 15, y2_rect - 16)
    
def mark_Injectors(pdf): # Форсунки
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 45
    y1 = 40
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 20, y1 - 5)

def make_Fuel_priming_pump(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 118
    y1 = 84
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 + 5)
    pdf.line(x1 + 5, y1 + 5, x1 + 30, y1 + 5)


def make_Oil_pump(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 184
    y1 = 41
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 20, y1 - 5)


def make_Oil_filter(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 34
    y1 = 42
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 + 5)
    pdf.line(x1 + 5, y1 + 5, x1 + 20, y1 + 5)


def make_Cooling_fan(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 178
    y1 = 35
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 20, y1 - 5)


def make_Coolant_pump(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 24
    y1 = 41
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 + 10)
    pdf.line(x1 + 5, y1 + 10, x1 + 24, y1 + 10)


def make_Radiator(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 21
    y1 = 42
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 + 13)
    pdf.line(x1 + 5, y1 + 13, x1 + 24, y1 + 13)


def make_Radiator_cap(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 21
    y1 = 34
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 8)
    pdf.line(x1 + 5, y1 - 8, x1 + 22, y1 - 8)


def make_Pistons(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 34
    y1 = 81
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 17, y1 - 5)

def make_Connecting_rod(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 34
    y1 = 86
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 28, y1 - 5)


def make_Crankshaft(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 32
    y1 = 83
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 12)
    pdf.line(x1 + 5, y1 - 12, x1 + 21, y1 - 12)


def make_Flywheel(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 48
    y1 = 92
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 20, y1 - 5)


def make_Cylinder_head(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 32
    y1 = 35
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 5)
    pdf.line(x1 + 5, y1 - 5, x1 + 20, y1 - 5)


def make_Valve_drive(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)

    pdf.set_fill_color(255, 0, 0)

    x1 = 25
    y1 = 83
    pdf.ellipse(x1, y1, 2, 2, 'F')
 
    pdf.line(x1 + 1, y1 + 1, x1 + 5, y1 - 18)
    pdf.line(x1 + 5, y1 - 18, x1 + 21, y1 - 18)


def set_labels(pdf, nodes):
    pdf.set_font("Arial", 'B', size=8)

    if any("High_pressure_pump" in n for n in nodes):
        pdf.text(121, 79, "High pressure pump")
    if any("Fuel_filter" in n for n in nodes):
        pdf.text(121, 73, "Fuel filter")
    if any("Injectors" in n for n in nodes):
        pdf.text(52, 34, "Injectors")
    if any("Fuel_priming_pump" in n for n in nodes):
        pdf.text(123, 87, "Fuel priming pump")
    if any("Oil_pump" in n for n in nodes):
        pdf.text(190, 35, "Oil pump")
    if any("Oil_filter" in n for n in nodes):
        pdf.text(40, 46, "Oil filter")
    if any("Cooling_fan" in n for n in nodes):
        pdf.text(184, 29, "Cooling fan")
    if any("Coolant_pump" in n for n in nodes):
        pdf.text(29, 50, "Cooling pump")
    if any("Radiator" in n for n in nodes):
        pdf.text(29, 54, "Radiator")
    if any("Radiator_cap" in n for n in nodes):
        pdf.text(26, 25, "Radiator cap")
    if any("Pistons" in n for n in nodes):
        pdf.text(40, 75, "Pistons")
    if any("Connecting_rod" in n for n in nodes):
        pdf.text(40, 80, "Connecting_rod")
    if any("Crankshaft" in n for n in nodes):
        pdf.text(38, 70, "Crankshaft")
    if any("Flywheel" in n for n in nodes):
        pdf.text(55, 86, "Flywheel")
    if any("Cylinder_head" in n for n in nodes):
        pdf.text(38, 29, "Cylinder head")
    if any("Valve_drive" in n for n in nodes):
        pdf.text(31, 64, "Valve drive")
    

def generate_table(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    
    if sys.argv[1] != '':
        data  = [['Vehicle Node Name', 'Probability of malfunction']]
        for i in range(1, len(sys.argv), 2):
            data.append([sys.argv[i], str(100 - int(sys.argv[i + 1])) ])
        
        print("Appended data: ", data)
        
        pdf.ln(10)
        spacing = 1
        col_width = pdf.w / 3.5
        row_height = pdf.font_size * 1.8
        for row in data:
            for item in row:
                pdf.cell(col_width, row_height*spacing,
                        txt=item, border=1)
            pdf.ln(row_height*spacing)

def create_table_evidences(pdf):
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font('Arial', 'I', 18)
    pdf.ln()
    pdf.cell(0, 5, 'Evidences', 0, 0, 'C')
    pdf.ln()

    pdf.set_font("Arial", 'B', size=8)

    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)

    data = [["Name"]]

    with open('..\\evidences.txt', 'r') as f:
        evidences = f.readlines() 
        for line in evidences: 
            data.append([line.replace('_', ' ')])

    pdf.ln(10)
    spacing = 1
    col_width = pdf.w / 2.5
    row_height = pdf.font_size * 1.8
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                    txt=item, border=1)
        pdf.ln(row_height*spacing)

        
def main():
    pdf = FPDF()
    pdf.add_page()

    pdf.image('Car_diagram.jpg', x = None, y = None, w = 200, h = 100, type = '', link = '')
    
    nodes = []
    for i in range(1, len(sys.argv), 2):
        nodes.append(sys.argv[i])


    if any("High_pressure_pump" in n for n in nodes):
        mark_High_pressure_pump(pdf)
    if any("Fuel_filter" in n for n in nodes):
        mark_Fuel_filter(pdf)
    if any("Injectors" in n for n in nodes):
        mark_Injectors(pdf)
    if any("Fuel_priming_pump" in n for n in nodes):
        make_Fuel_priming_pump(pdf)
    if any("Oil_pump" in n for n in nodes):
        make_Oil_pump(pdf)
    if any("Oil_filter" in n for n in nodes):
        make_Oil_filter(pdf)
    if any("Cooling_fan" in n for n in nodes):
        make_Cooling_fan(pdf)
    if any("Coolant_pump" in n for n in nodes):
        make_Coolant_pump(pdf)
    if any("Radiator" in n for n in nodes):
        make_Radiator(pdf)
    if any("Radiator_cap" in n for n in nodes):
        make_Radiator_cap(pdf)
    if any("Pistons" in n for n in nodes):
        make_Pistons(pdf)
    if any("Connecting_rod" in n for n in nodes):
        make_Connecting_rod(pdf)
    if any("Crankshaft" in n for n in nodes):
        make_Crankshaft(pdf)
    if any("Flywheel" in n for n in nodes):
        make_Flywheel(pdf)
    if any("Cylinder_head" in n for n in nodes):
        make_Cylinder_head(pdf)
    if any("Valve_drive" in n for n in nodes):
        make_Valve_drive(pdf)

    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font('Arial', 'I', 18)
    pdf.cell(0, 5, 'Critical nodes reports', 0, 0, 'C')

    set_labels(pdf, nodes)
    generate_table(pdf)
    create_table_evidences(pdf)
    pdf.add_page()

    file_list=[f for f in os.listdir(r"..\\RandomForest\\") if f.endswith('.png')]
    print(file_list)
    
    pdf.set_line_width(1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font('Arial', 'I', 15)

    for filename in file_list:
        if filename.find("Result") != -1:
            pdf.cell(0, 15, filename.replace('Result', '').replace('.png', '').replace('_', ' '), 0, 0, 'C')
            pdf.ln()
        pdf.image('..\\RandomForest\\' + str(filename), x = None, y = None, w = 200, h = 120, type = '', link = '')

    pdf.output("Report.pdf")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()