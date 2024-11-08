import beautifuljason as bjason
import h5py

# python -m SBR_analysis

# Initialize variables
file1 = 'C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/2-ethyl-1-indanone 1_PROTON-1-1.jdf'
file2 = 'C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/2-ethyl-1-indanone 1_PROTON-1-1.jdf'
rules_name = 'ISO_SBR'


# Initialize JASON object
jason = bjason.JASON()

# Create, close, and copy the document with an absolute path for the rules file
with jason.create_document(file1, 
                           rules=rules_name) as doc:
    doc.close()
    doc.copy('C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/simple_integral_example.jjh5')
    
with jason.create_document(file2, 
                           rules=rules_name) as doc2:
    doc2.close()
    doc2.copy('C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/simple_integral_example2.jjh5')

# Open the Jason file, read the integral and print them
with h5py.File('C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/simple_integral_example.jjh5', 'r') as h5_file:
    multiplet1 = bjason.NMRMultiplet(h5_file['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/0'])
    int_C_file1 = multiplet1.value
    print('Integral C is : ', multiplet1.value)
    multiplet2 = bjason.NMRMultiplet(h5_file['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/1'])
    int_B_file1 = multiplet2.value
    print('Integral B is : ', multiplet2.value)
    multiplet3 = bjason.NMRMultiplet(h5_file['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/2'])
    int_A_file1 = multiplet3.value
    print('Integral A is : ', multiplet3.value)
    multiplet4 = bjason.NMRMultiplet(h5_file['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/3'])
    int_TMS_file1 = multiplet4.value
    print('Integral TMS is : ', multiplet4.value)
    h5_file.close()

with h5py.File('C:/Users/Botana.SERVDOMAIN2/Desktop/python_qc/simple_integral_example2.jjh5', 'r') as h5_file2:
    multiplet1 = bjason.NMRMultiplet(h5_file2['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/0'])
    int_C_file2 = multiplet1.value
    print('Integral C blank is : ', multiplet1.value)
    multiplet2 = bjason.NMRMultiplet(h5_file2['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/1'])
    int_B_file2 = multiplet2.value
    multiplet3 = bjason.NMRMultiplet(h5_file2['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/2'])
    int_A_file2 = multiplet3.value
    multiplet4 = bjason.NMRMultiplet(h5_file2['/JasonDocument/NMR/NMRData/0/Multiplets_Integrals/MultipletList/3'])
    int_TMS_file2 = multiplet4.value
    print('Integral TMS blank is : ', multiplet2.value)
    h5_file.close()
    
c_calib = int_C_file1 - int_C_file2*int_TMS_file1/int_TMS_file2
s_m = c_calib*104/5*100/(c_calib*104/5+(int_B_file1/2+int_A_file1/4)*54)
v_ = int_A_file1/2*100/(int_B_file1/2+int_A_file1/4)
tc_ = (int_B_file1/2-int_A_file1/4)/(int_B_file1/2+int_A_file1/4)*100


print('Normalized integral C is : ', c_calib)

print('')
print('========================================================================')
print('Styrene content is :                     ', s_m, ' % mass')
print('Vinyl content of butadiene is :          ', v_, ' % molar')
print('Trans and cis content of butadiene is :  ', tc_, ' % molar')
print('========================================================================')
print('')
