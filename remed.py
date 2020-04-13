def ceknpwp(npwp):
    nomor = '0123456789-.'
    status = True
    
    for i in npwp:
        if i not in nomor:
            status = False
            
    if '-' not in npwp and '.' not in npwp:
        status = False
    if status == False:
        return 'Kode seri NPWP tidak valid!'
        
    identitas = npwp[:2]
    regis = npwp[3:10]
    aman = npwp[11]
    kodeKPP = npwp[13:16]
    statuswp = npwp[17:]
    
    if status:
        print('Kode seri NPWP valid!')
        x = ['01','02','03','04','05','06','07','08','09']
        
        if identitas == '01' or identitas == '02' or identitas == '03':
            print('Identitas Wajib Pajak: ', identitas, 'Wajib Pajak Badan')
        elif identitas == '04' or identitas == '06':
            print('Identitas Wajib Pajak: ', identitas, 'Wajib Pajak Pengusaha')
        elif identitas == '05':
            print('Identitas Wajib Pajak: ', identitas, 'Wajib Pajak Karyawan')
        elif identitas == '07' or identitas == '08' or identitas == '09':
            print('Identitas Wajib Pajak: ', identitas, 'Wajib Pajak Orang Pribadi')
                        
        print('Nomor Registrasi: ', regis)            
        print('Alat pengaman: ', aman)
        print('Kode KPP: ', kodeKPP)      
        print('Status Wajib Pajak: ', statuswp)

    else:
        print('Kode seri NPWP tidak valid!')

ceknpwp('02.123.456.0-212.191')