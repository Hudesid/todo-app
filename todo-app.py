print('\nHush kelibsiz\n')
vazifa = {}
while True:
    print('\n1. Vazifani kritmoqchi bolsangiz (1) kriting.\n')
    print('2. Vazifani ochirmoqchi bolsangiz (2) kriting.\n')
    print('3. Vazifani kormoqchi bolsangiz (3) kriting.\n')
    print('4. Vazifani jarayondaligini kritish uchun (4) kriting.\n')
    print('5. Programadan chiqmoqchi bolsangiz (5) kriting.\n')
    raqam_kritish = int(input('Raqamni kriting:'))
    if raqam_kritish == 1:
        kalit = input('\nVazifani nomini kriting:')
        qiymati = input('Topshiriqni kriting:')
        vaqt = input('Vaqtni tugash kunini kriting:')
        jarayon = 'jarayon davom etyapti'
        vazifa[kalit] = [qiymati, vaqt, jarayon]
        print('\nVazifa muvaffaqiyatli kritildi!')
    elif raqam_kritish == 2:
        kalit = input('Ochirmoqchi bolgan vazifa nomini kriting:')
        if kalit in vazifa:
            del vazifa[kalit]
            print('\nVazifa muvaffaqiyatli ochirildi!')
        else:
            print('\nVazifa topilmadi.')
    elif raqam_kritish == 3:
        if len(vazifa) > 0:
            for kalit, detail in vazifa.items():
                print(f'\nVazifa nomi: {kalit}')
                print(f'Topshiriq: {detail[0]}')
                print(f'Vazifa tugash kuni: {detail[1]}')
                print(f'Vazifa holati: {detail[-1]}\n')
        else:
            print('\nVazifalar royxati bosh.')
    elif raqam_kritish == 4:
        kalit = input('Vazifa nomini kriting:')
        if kalit in vazifa:
            detail = vazifa[kalit]
            detail[-1] = 'Vazifa tugagan!'
            vazifa[kalit] = detail
            print('\nVazifa holati ozgardi!')
        else:
            print('\nVazifa topilmadi.')
    elif raqam_kritish == 5:
        print('\nProgramadan muvaffaqiyatli chiqdingiz.')
        break

