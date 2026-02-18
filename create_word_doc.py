"""
Script to create a Word document about Python Assignment Operators
"""

try:
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    # Create a new Document
    doc = Document()

    # Add title
    title = doc.add_heading('Python Assignment Operators Reference Guide', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Add subtitle
    subtitle = doc.add_paragraph('A Complete Guide for Beginners')
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].font.size = Pt(14)
    subtitle.runs[0].font.italic = True

    doc.add_paragraph()  # Empty line

    # Section 1: Basic Assignment
    doc.add_heading('1. Basic Assignment Operator', 1)

    doc.add_heading('= (Assignment)', 2)
    doc.add_paragraph('Description: Assigns a value to a variable.')
    doc.add_paragraph('Syntax: variable = value')

    code1 = doc.add_paragraph('x = 10\nname = "Peter"\nprice = 99.99')
    code1.style = 'Quote'

    # Section 2: Arithmetic Assignment Operators
    doc.add_heading('2. Arithmetic Assignment Operators', 1)
    doc.add_paragraph('These operators combine arithmetic operations with assignment.')

    # += operator
    doc.add_heading('+= (Add and Assign)', 2)
    doc.add_paragraph('Description: Adds the right value to the variable and assigns the result back.')
    doc.add_paragraph('Syntax: x += y  (equivalent to x = x + y)')
    code2 = doc.add_paragraph('score = 10\nscore += 5    # score is now 15\nscore += 3    # score is now 18')
    code2.style = 'Quote'

    # -= operator
    doc.add_heading('-= (Subtract and Assign)', 2)
    doc.add_paragraph('Description: Subtracts the right value from the variable.')
    doc.add_paragraph('Syntax: x -= y  (equivalent to x = x - y)')
    code3 = doc.add_paragraph('lives = 3\nlives -= 1    # lives is now 2\nlives -= 1    # lives is now 1')
    code3.style = 'Quote'

    # *= operator
    doc.add_heading('*= (Multiply and Assign)', 2)
    doc.add_paragraph('Description: Multiplies the variable by the right value.')
    doc.add_paragraph('Syntax: x *= y  (equivalent to x = x * y)')
    code4 = doc.add_paragraph('points = 10\npoints *= 2    # points is now 20\npoints *= 3    # points is now 60')
    code4.style = 'Quote'

    # /= operator
    doc.add_heading('/= (Divide and Assign)', 2)
    doc.add_paragraph('Description: Divides the variable by the right value.')
    doc.add_paragraph('Syntax: x /= y  (equivalent to x = x / y)')
    doc.add_paragraph('Note: Always results in a float.')
    code5 = doc.add_paragraph('total = 100\ntotal /= 2    # total is now 50.0\ntotal /= 5    # total is now 10.0')
    code5.style = 'Quote'

    # //= operator
    doc.add_heading('//= (Floor Divide and Assign)', 2)
    doc.add_paragraph('Description: Divides and rounds down to the nearest whole number.')
    doc.add_paragraph('Syntax: x //= y  (equivalent to x = x // y)')
    doc.add_paragraph('Use Case: When you need whole numbers only.')
    code6 = doc.add_paragraph('items = 17\nitems //= 5    # items is now 3')
    code6.style = 'Quote'

    # %= operator
    doc.add_heading('%= (Modulus and Assign)', 2)
    doc.add_paragraph('Description: Gets the remainder of division.')
    doc.add_paragraph('Syntax: x %= y  (equivalent to x = x % y)')
    doc.add_paragraph('Use Case: Check if a number is even/odd, find leftover items.')
    code7 = doc.add_paragraph('remainder = 17\nremainder %= 5    # remainder is now 2')
    code7.style = 'Quote'

    # **= operator
    doc.add_heading('**= (Exponent and Assign)', 2)
    doc.add_paragraph('Description: Raises the variable to a power.')
    doc.add_paragraph('Syntax: x **= y  (equivalent to x = x ** y)')
    doc.add_paragraph('Use Case: Calculating powers, areas, BMI calculations.')
    code8 = doc.add_paragraph('base = 2\nbase **= 3    # base is now 8 (2³ = 8)')
    code8.style = 'Quote'

    # Section 3: Quick Reference
    doc.add_page_break()
    doc.add_heading('3. Quick Reference Table', 1)

    # Create table
    table = doc.add_table(rows=9, cols=4)
    table.style = 'Light Grid Accent 1'

    # Header row
    headers = ['Operator', 'Name', 'Long Form', 'Short Form']
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True

    # Data rows
    data = [
        ['=', 'Assignment', 'x = 5', 'x = 5'],
        ['+=', 'Add Assign', 'x = x + 5', 'x += 5'],
        ['-=', 'Subtract Assign', 'x = x - 3', 'x -= 3'],
        ['*=', 'Multiply Assign', 'x = x * 2', 'x *= 2'],
        ['/=', 'Divide Assign', 'x = x / 4', 'x /= 4'],
        ['//=', 'Floor Divide Assign', 'x = x // 2', 'x //= 2'],
        ['%=', 'Modulus Assign', 'x = x % 3', 'x %= 3'],
        ['**=', 'Exponent Assign', 'x = x ** 2', 'x **= 2']
    ]

    for i, row_data in enumerate(data, start=1):
        for j, value in enumerate(row_data):
            table.rows[i].cells[j].text = value

    # Section 4: Practical Examples
    doc.add_heading('4. Practical Examples', 1)

    doc.add_heading('Example 1: Shopping Cart', 2)
    ex1 = doc.add_paragraph(
        'cart_total = 0\n'
        'cart_total += 29.99    # Add item 1\n'
        'cart_total += 15.50    # Add item 2\n'
        'cart_total += 8.25     # Add item 3\n'
        'print(f"Total: ${cart_total}")  # Total: $53.74'
    )
    ex1.style = 'Quote'

    doc.add_heading('Example 2: Game Score', 2)
    ex2 = doc.add_paragraph(
        'score = 100\n'
        'score *= 2         # Double points\n'
        'score += 50        # Collect coins\n'
        'print(f"Score: {score}")  # Score: 250'
    )
    ex2.style = 'Quote'

    doc.add_heading('Example 3: BMI Calculator', 2)
    ex3 = doc.add_paragraph(
        'weight = 70        # kg\n'
        'height = 1.75      # meters\n'
        'height **= 2       # Square the height\n'
        'bmi = weight / height\n'
        'print(f"BMI: {bmi:.2f}")  # BMI: 22.86'
    )
    ex3.style = 'Quote'

    doc.add_heading('Example 4: Check Even or Odd', 2)
    ex4 = doc.add_paragraph(
        'number = 17\n'
        'check = number\n'
        'check %= 2         # Get remainder\n'
        'if check == 0:\n'
        '    print("Even")\n'
        'else:\n'
        '    print("Odd")   # Output: Odd'
    )
    ex4.style = 'Quote'

    # Section 5: Common Mistakes
    doc.add_page_break()
    doc.add_heading('5. Common Mistakes to Avoid', 1)

    doc.add_heading('Mistake 1: Using == instead of =', 2)
    m1 = doc.add_paragraph('# Wrong\nx == 5    # This checks, doesn\'t assign!\n\n# Correct\nx = 5     # This assigns')
    m1.style = 'Quote'

    doc.add_heading('Mistake 2: Not initializing variables', 2)
    m2 = doc.add_paragraph('# Wrong\ntotal += 10   # Error if total doesn\'t exist\n\n# Correct\ntotal = 0     # Initialize first\ntotal += 10   # Now it works')
    m2.style = 'Quote'

    # Section 6: Tips
    doc.add_heading('6. Tips for Beginners', 1)

    tips = [
        'Always initialize variables before using assignment operators',
        'Use meaningful variable names',
        'Remember that assignment operators modify the original variable',
        'You can chain operations (e.g., x += 5 then x *= 2)'
    ]

    for tip in tips:
        doc.add_paragraph(tip, style='List Bullet')

    # Section 7: Summary
    doc.add_heading('7. Summary', 1)

    summary = doc.add_paragraph()
    summary.add_run('Assignment operators are shortcuts that make your code:\n').bold = True
    doc.add_paragraph('Shorter - Less typing', style='List Bullet')
    doc.add_paragraph('Cleaner - Easier to read', style='List Bullet')
    doc.add_paragraph('Professional - Industry standard', style='List Bullet')
    doc.add_paragraph('Safer - Less chance of typos', style='List Bullet')

    doc.add_paragraph()
    conclusion = doc.add_paragraph('Instead of writing ')
    conclusion.add_run('total = total + 10').italic = True
    conclusion.add_run(', simply write ')
    conclusion.add_run('total += 10').italic = True
    conclusion.add_run('!')

    # Footer
    doc.add_paragraph()
    doc.add_paragraph()
    footer = doc.add_paragraph('Created for UDEMY Python Course')
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.runs[0].font.size = Pt(10)
    footer.runs[0].font.italic = True

    date_para = doc.add_paragraph('February 6, 2026')
    date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_para.runs[0].font.size = Pt(10)
    date_para.runs[0].font.italic = True

    # Save the document
    doc.save('Python_Assignment_Operators_Reference.docx')
    print("✅ Success! Word document created: Python_Assignment_Operators_Reference.docx")
    print("📁 Location: UDEMY_COURSE folder")
    print("📖 You can now open it in Microsoft Word!")

except ImportError:
    print("❌ Error: python-docx library not installed")
    print("📦 Installing python-docx...")
    print("\nPlease run: pip install python-docx")
    print("Then run this script again.")
except Exception as e:
    print(f"❌ Error: {e}")
