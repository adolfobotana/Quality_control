import beautifuljason as bjason

# python -m SBR_analysis_solventsubstraction

# Initialize variables
file1 = 'C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/SBR_proton-1-1.jdf'
rules_name = 'ISO_SBR'


# Initialize JASON object
jason = bjason.JASON()

# Open the file and apply the rules
with jason.create_document(file1, rules=rules_name) as doc:
    spec = doc.nmr_data[0]

# Extract the integrals and print the with 2 decimals   
    multiplet1 = spec.multiplets[0]
    int_C_file1 = multiplet1.value_hz
    print('C Integral is :      ', "{:.2f}".format(int_C_file1))
    multiplet2 = spec.multiplets[1]
    int_B_file1 = multiplet2.value_hz
    print('B Integral is :      ', "{:.2f}".format(int_B_file1))
    multiplet3 = spec.multiplets[2]
    int_A_file1 = multiplet3.value_hz
    print('A Integral is :       ', "{:.2f}".format(int_A_file1))
    multiplet4 = spec.multiplets[3]
    int_TMS_file1 = multiplet4.value_hz
    print('TMS Integral is :    ', "{:.2f}".format(int_TMS_file1))

# Find the solvent peak and extract its area (assuming it is only one peak, otherwise keep adding the areas of each solvent peak and/or impurities)   
    solvent = None
    for peak in spec.peaks:
        # if peak.classification == 2: # see classification at https://www.jeoljason.com/beautifuljason/docs/source/beautifuljason.data.html
        if peak.classification == bjason.NMRPeak.PeakClassification.NMRSolvent: 
            solvent = peak
            break
    int_solvent = solvent.area        
    print('Solvent Integral is : ', "{:.2f}".format(solvent.area), ' at ', "{:.2f}".format(solvent.pos[0]), ' ppm')

    # Uncomment the below lines to save the document
    # doc.close()
    # doc.copy('C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/simple_integral_example.jjh5')

# Subtract the solvent area from C integral
c_calib = int_C_file1 - int_solvent

# Calculate concentrations
s_m = c_calib*104/5*100/(c_calib*104/5+(int_B_file1/2+int_A_file1/4)*54)
v_ = int_A_file1/2*100/(int_B_file1/2+int_A_file1/4)
tc_ = (int_B_file1/2-int_A_file1/4)/(int_B_file1/2+int_A_file1/4)*100


print('')
print('========================================================================')
print('    Styrene content is :                     ', "{:.2f}".format(s_m), ' % mass')
print('    Vinyl content of butadiene is :          ', "{:.2f}".format(v_), ' % molar')
print('    Trans and cis content of butadiene is :  ', "{:.2f}".format(tc_), ' % molar')
print('========================================================================')
print('')
